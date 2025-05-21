import streamlit as st # Importa a biblioteca Streamlit.
import google.generativeai as genai # Importa a biblioteca para interagir com a IA do Google Gemini.

# Configurações básicas da página, como o layout e o título da aba do navegador.
st.set_page_config(layout="centered", page_title="REAL? | Checagem")

st.title("Checagem de Informações") # Título da página de Checagem.
st.write("Cole o texto, link ou envie um arquivo para verificar a veracidade.") # Instrução para o usuário.

# --- Integração com a IA Google Gemini ---
# Verifica se a chave de API do Gemini está disponível nos "segredos" do Streamlit.
# As chaves de API devem ser guardadas em um arquivo .streamlit/secrets.toml (veja a Etapa 4).
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Chave de API do Google Gemini não encontrada. Por favor, adicione-a em `.streamlit/secrets.toml`.")
    st.stop() # Interrompe a execução para evitar erros se a chave não estiver configurada.
else:
    # Configura a API do Gemini com a chave secreta.
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Inicializa o modelo de IA que usaremos (ex: 'gemini-pro' para texto).
    model = genai.GenerativeModel('gemini-pro')

# Cria uma área de texto onde o usuário pode inserir a informação.
user_input = st.text_area("Insira a informação aqui:", height=150)

# Cria um botão para iniciar a verificação.
if st.button("Verificar"):
    if user_input: # Verifica se o usuário inseriu algum texto.
        # Mostra uma mensagem de "carregando" enquanto a IA trabalha.
        with st.spinner("Analisando a informação..."):
            try:
                # Define o prompt (a instrução) para a IA.
                # Pedimos para a IA analisar, resumir e checar a veracidade.
                prompt = f"Analise a seguinte informação para checar sua veracidade e forneça um resumo conciso (3-4 parágrafos) com base em fontes confiáveis. Se possível, cite as fontes. Informação: '{user_input}'"
                # Envia o prompt para o modelo Gemini e obtém a resposta.
                response = model.generate_content(prompt)
                st.subheader("Resultado da Checagem:") # Subtítulo para o resultado.
                st.write(response.text) # Exibe a resposta da IA.

                # Aqui seria o local para adicionar o botão de leitura em áudio.
                # st.button("Ouvir Checagem") # Este botão exigiria uma biblioteca adicional (ex: gTTS) e lógica para reproduzir o áudio.
                # Por enquanto, é apenas um placeholder.

            except Exception as e: # Captura qualquer erro que possa ocorrer na comunicação com a IA.
                st.error(f"Ocorreu um erro ao processar sua solicitação: {e}")
                st.info("Verifique se a chave de API está correta e se a informação não é muito complexa para o modelo.")
    else: # Se o usuário não inseriu nada, exibe um aviso.
        st.warning("Por favor, insira alguma informação para verificar.")

# Botão para voltar à página inicial, usando um link direto para o arquivo Home.py.
# st.page_link("Home.py", label="Voltar ao Início", icon="🏠") # O Streamlit cria automaticamente a navegação, então este botão pode ser opcional.
import streamlit as st # Importa a biblioteca Streamlit.
import google.generativeai as genai # Importa a biblioteca para interagir com a IA do Google Gemini.

# Configurações básicas da página.
st.set_page_config(layout="centered", page_title="REAL? | Dicas")

st.title("Dicas para o Pensamento Crítico") # Título da página.
st.write("Aprenda a avaliar a credibilidade de uma informação e desenvolva seu senso crítico.") # Descrição.

# --- Integração com a IA Google Gemini ---
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Chave de API do Google Gemini não encontrada. Por favor, adicione-a em `.streamlit/secrets.toml`.")
    st.stop()
else:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')

# Lista de dicas estáticas (ou podem ser geradas por IA no futuro).
# Para o MVP, começamos com algumas dicas fixas e as perguntas serão geradas pela IA.
dicas = [
    "Verifique a fonte: Quem publicou a informação? É um veículo conhecido e confiável?",
    "Analise a data: A notícia é recente ou é um fato antigo sendo recirculado?",
    "Leia além do título: Títulos podem ser sensacionalistas. Leia o conteúdo completo.",
    "Procure por evidências: Há dados, estudos ou citações que comprovem a informação?",
    "Compare com outras fontes: Outras fontes de notícias confiáveis estão reportando o mesmo?",
    "Cuidado com o apelo emocional: Notícias falsas frequentemente usam linguagem que provoca raiva ou medo.",
]

st.subheader("Avalie a Informação com Estas Dicas:") # Subtítulo.

for i, dica in enumerate(dicas): # Itera sobre cada dica na lista.
    # Cria uma seção que pode ser expandida/contraída para cada dica.
    with st.expander(f"Dica {i+1}: {dica.split(':')[0]}"):
        st.write(dica) # Exibe a dica completa.
        # Botão para gerar perguntas reflexivas sobre a dica.
        if st.button(f"Gere perguntas para refletir ({i+1})", key=f"q_btn_{i}"):
            with st.spinner("Gerando perguntas..."):
                try:
                    # Prompt para a IA gerar perguntas que incentivem a reflexão.
                    reflection_prompt = f"Gere 2 a 3 perguntas que incitem o usuário a refletir sobre como aplicar a dica '{dica}' ao consumir informações. As perguntas devem ser incitadoras, não julgadoras. Formate como uma lista."
                    reflection_response = model.generate_content(reflection_prompt)
                    st.info(reflection_response.text) # Exibe as perguntas geradas.
                except Exception as e:
                    st.error(f"Erro ao gerar perguntas: {e}")
                    st.info("Tente novamente ou verifique a API.")

# st.page_link("Home.py", label="Voltar ao Início", icon="🏠")
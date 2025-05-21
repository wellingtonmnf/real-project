import streamlit as st # Importa a biblioteca Streamlit.
import google.generativeai as genai # Importa a biblioteca para interagir com a IA do Google Gemini.

# Configurações básicas da página.
st.set_page_config(layout="centered", page_title="REAL? | Relatos")

st.title("Relatos de Impacto") # Título da página de Relatos.
st.write("Veja como a desinformação afeta vidas reais através de relatos reais (gerados por IA para fins de exemplo).") # Descrição.

# --- Integração com a IA Google Gemini ---
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Chave de API do Google Gemini não encontrada. Por favor, adicione-a em `.streamlit/secrets.toml`.")
    st.stop()
else:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')

# Botão para gerar novos relatos.
if st.button("Gerar Novos Relatos"):
    with st.spinner("Buscando relatos..."): # Mostra um "carregando".
        try:
            # Prompt para a IA gerar relatos. Pedimos 3 a 5 relatos fictícios.
            prompt = "Gere de 3 a 5 relatos concisos e impactantes (máximo 2-3 frases por relato) de vítimas de golpes, fraudes ou situações de risco causadas por desinformação. Crie cenários diversos e evite nomes de pessoas reais. Formate cada relato como um parágrafo separado. Exemplo: 'Fui enganado por uma notícia falsa sobre um investimento milagroso e perdi minhas economias de anos.'"
            response = model.generate_content(prompt) # Envia o prompt para a IA.
            st.subheader("Relatos Recentes:") # Subtítulo.
            st.write(response.text) # Exibe os relatos gerados.
        except Exception as e:
            st.error(f"Ocorreu um erro ao gerar os relatos: {e}")
            st.info("Verifique sua conexão e chave de API.")

# st.page_link("Home.py", label="Voltar ao Início", icon="🏠")
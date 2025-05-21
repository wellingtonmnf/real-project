import streamlit as st # Importa a biblioteca Streamlit.
import google.generativeai as genai # Importa a biblioteca para interagir com a IA do Google Gemini.

# Configurações básicas da página.
st.set_page_config(layout="centered", page_title="REAL? | Alertas")

st.title("Alertas de Golpes e Fraudes") # Título da página.
st.write("Fique atento aos tipos mais comuns e recentes de golpes veiculados por desinformação.") # Descrição.

# --- Integração com a IA Google Gemini ---
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Chave de API do Google Gemini não encontrada. Por favor, adicione-a em `.streamlit/secrets.toml`.")
    st.stop()
else:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')

# Lista de alertas (inicialmente vazia, será populada pela IA ou por dados estáticos).
# Para o MVP, podemos gerar alertas com IA.
if st.button("Gerar Alertas Atuais"):
    with st.spinner("Buscando alertas..."):
        try:
            # Prompt para a IA gerar alertas de golpes comuns.
            alert_prompt = "Gere 3 a 5 alertas concisos sobre golpes comuns veiculados por desinformação, cada um com uma frase curta de como se proteger. Use um formato de lista numerada. Exemplo: '1. Golpe do falso emprego: Desconfie de vagas com salários muito altos e sem experiência.'"
            alerts_response = model.generate_content(alert_prompt)
            alerts = alerts_response.text.split('\n') # Divide a resposta em linhas para cada alerta.

            # Para cada alerta, cria uma seção expansível.
            for i, alert in enumerate(alerts):
                if alert.strip(): # Garante que a linha não esteja vazia
                    # Cria uma seção que pode ser expandida/contraída.
                    with st.expander(f"Alerta: {alert.split(':')[0]}"):
                        st.write(alert) # Mostra o alerta completo.
                        # Botão para gerar um exemplo hipotético do golpe.
                        if st.button(f"Me dê um exemplo disto ({i+1})", key=f"ex_btn_{i}"):
                            with st.spinner("Gerando exemplo..."):
                                try:
                                    example_prompt = f"Crie uma breve situação hipotética (1-2 parágrafos) que ilustre o seguinte golpe: '{alert}'. Não mencione nomes reais."
                                    example_response = model.generate_content(example_prompt)
                                    st.info(example_response.text) # Exibe o exemplo.
                                except Exception as e:
                                    st.error(f"Erro ao gerar exemplo: {e}")
                                    st.info("Tente novamente ou verifique a API.")
        except Exception as e:
            st.error(f"Ocorreu um erro ao gerar os alertas: {e}")
            st.info("Verifique sua conexão e chave de API.")

# st.page_link("Home.py", label="Voltar ao Início", icon="🏠")
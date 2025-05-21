import streamlit as st # Importa a biblioteca Streamlit, que nos permite criar a interface web.

# Configurações básicas da página, como o layout e o título que aparece na aba do navegador.
# O layout "wide" tenta usar mais da largura da tela.
st.set_page_config(layout="centered", page_title="REAL? | Home")

# st.image("caminho/para/logo.png", width=100) # Se tiver um logo no futuro, pode descomentar e usar.

st.title("REAL?") # Exibe o título principal da nossa aplicação na página.
st.write("---") # Desenha uma linha horizontal para separar visualmente elementos.

# Texto introdutório da homepage, explicando o propósito da plataforma.
st.subheader("Discernindo a verdade no mundo digital")
st.write("Nossa plataforma te ajuda a checar informações, entender relatos de desinformação, receber alertas sobre golpes e desenvolver seu pensamento crítico.")
st.write("---")

# Rodapé da aplicação, com informações sobre o desenvolvedor e a IA utilizada.
st.caption("Desenvolvido com o poder da IA Generativa (Google Gemini)")
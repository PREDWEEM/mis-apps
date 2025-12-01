# ================================================================
# 🌾 PREDWEEM — EJECUCIÓN DIRECTA DEL HTML DENTRO DE STREAMLIT
# ================================================================

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ---------------------------------------------------------------
# CONFIG STREAMLIT
# ---------------------------------------------------------------
st.set_page_config(
    page_title="PREDWEEM – Predictive Weed Emergence Models",
    layout="wide",
)

st.markdown("""
<style>
/* Eliminar menú, barra superior y footer de Streamlit */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------------
# CARGAR ARCHIVO HTML
# ---------------------------------------------------------------
HTML_PATH = Path("index.html")

if not HTML_PATH.exists():
    st.error("⚠ No se encontró el archivo index.html en el mismo directorio que app.py")
    st.stop()

html_code = HTML_PATH.read_text(encoding="utf-8")

# ---------------------------------------------------------------
# RENDERIZAR HTML COMPLETO
# ---------------------------------------------------------------
components.html(
    html_code,
    height=5000,    # Ajustar si tu HTML es más largo
    scrolling=True
)


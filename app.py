# ================================================================
# 🌾 PREDWEEM · Modern Streamlit Wrapper for Full HTML Websites
# ---------------------------------------------------------------
# - Renderiza index.html COMPLETO (CSS + JS + imágenes)
# - Compatible Streamlit Cloud
# - Layout moderno y responsivo
# - Incluye soporte para archivos estáticos
# ================================================================

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ---------------------------------------------------------------
# 🔧 Configuración general
# ---------------------------------------------------------------
st.set_page_config(
    page_title="PREDWEEM – Weed Emergence Models",
    layout="wide",
)

# ---------------------------------------------------------------
# 🖼 Estilos propios de la app (no interfieren con el HTML)
# ---------------------------------------------------------------
st.markdown("""
<style>
/* Fondo más moderno */
.stApp {
    background: #f5f6f2;
}

/* Contenedor principal */
.wrapper {
    max-width: 1400px;
    margin-left: auto;
    margin-right: auto;
    padding: 10px 20px;
}

/* Marco elegante del iframe */
.html-frame {
    border: 1px solid #d7ddcc;
    border-radius: 14px;
    box-shadow: 0px 2px 12px rgba(0,0,0,0.12);
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# 📌 Cargar HTML desde archivo local
# ---------------------------------------------------------------
HTML_PATH = Path("index.html")

if not HTML_PATH.exists():
    st.error("❌ No se encuentra el archivo **index.html** en el directorio raíz del proyecto.")
    st.stop()

html_content = HTML_PATH.read_text(encoding="utf-8")

# ---------------------------------------------------------------
# 🚀 INTERFAZ: Header minimalista (marca + descripción)
# ---------------------------------------------------------------
with st.container():
    st.markdown("""
        <div class="wrapper">
            <h1 style="color:#2e5e2d; font-size:38px; margin-bottom:0;">
                🌾 PREDWEEM – Predictive Weed Emergence Models
            </h1>
            <p style="color:#546054; font-size:18px; margin-top:4px;">
                Plataforma integrada para modelos de emergencia de malezas,
                desarrollado por UNS · INTA · CERZOS · UNICEN.
            </p>
            <hr style="margin-top:10px; margin-bottom:20px; border-color:#ccd5c2;">
        </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------------
# 🌐 Renderiza el HTML completo dentro de un iframe responsivo
# ---------------------------------------------------------------
with st.container():
    st.markdown('<div class="wrapper"><div class="html-frame">', unsafe_allow_html=True)

    components.html(
        html_content,
        height=2200,        # Ajustá según tamaño real de tu HTML
        scrolling=True
    )

    st.markdown('</div></div>', unsafe_allow_html=True)

# ---------------------------------------------------------------
# 🦶 Footer profesional
# ---------------------------------------------------------------
st.markdown("""
<br><br>
<div style="text-align:center; color:#6e7a6c; font-size:14px;">
    © 2025 · PREDWEEM – Plataforma de Modelos Predictivos de Emergencia · Todos los derechos reservados.
</div>
""", unsafe_allow_html=True)

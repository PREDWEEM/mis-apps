# ================================================================
# 🌾 PREDWEEM — Render HTML con imágenes que SI cargan (BASE64)
# ================================================================

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
import re

# ---------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------
st.set_page_config(page_title="PREDWEEM", layout="wide")

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# FUNCIONES
# ---------------------------------------------------------------

def img_to_base64(path: Path) -> str:
    """Convierte un archivo de imagen a una cadena base64."""
    if not path.exists():
        return None
    data = path.read_bytes()
    return base64.b64encode(data).decode("utf-8")

def replace_images_with_base64(html: str, base_dir: Path) -> str:
    """
    Busca <img src="archivo.ext"> y reemplaza por Base64
    para que Streamlit pueda cargarlas dentro del iframe.
    """
    def repl(match):
        filename = match.group(1)
        img_path = base_dir / filename
        b64 = img_to_base64(img_path)

        if b64 is None:
            # Imagen no encontrada → dejar texto alternativo
            return f'<img alt="No se encontró {filename}">'

        # Detecta formato según extensión
        ext = filename.split(".")[-1].lower()
        mime = "jpeg" if ext in ["jpg", "jpeg"] else ext

        return f'<img src="data:image/{mime};base64,{b64}" />'

    # Reemplaza solo las etiquetas <img src="...">
    return re.sub(r'<img[^>]*src=["\']([^"\']+)["\']', repl, html)


# ---------------------------------------------------------------
# CARGAR Y PROCESAR index.html
# ---------------------------------------------------------------

HTML_PATH = Path("index.html")
BASE_DIR = Path(".")

if not HTML_PATH.exists():
    st.error("⚠ No se encontró index.html en el directorio raíz.")
    st.stop()

html_code = HTML_PATH.read_text(encoding="utf-8")

# Reemplazar imágenes por base64
html_code = replace_images_with_base64(html_code, BASE_DIR)

# ---------------------------------------------------------------
# RENDER FINAL
# ---------------------------------------------------------------
components.html(
    html_code,
    height=6000,
    scrolling=True
)


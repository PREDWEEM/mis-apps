
# =========================================================
# 🌾 PREDWEEM – Landing simplificada y robusta para Streamlit
# - Sin JS, sin HTML complejo
# - Con captura de errores para evitar "Error running app"
# =========================================================

import streamlit as st

# ---------------------------------------------------------
# CONFIGURACIÓN BÁSICA
# ---------------------------------------------------------
try:
    st.set_page_config(
        page_title="PREDWEEM – Predictive Weed Emergence Models",
        layout="wide"
    )
except Exception as e:
    # Si algo falla acá, lo mostramos y frenamos
    st.write("Error en set_page_config")
    st.exception(e)

st.title("🌾 PREDWEEM – Landing de prueba")
st.write(
    "Si estás viendo este texto, el app.py básico está funcionando. "
    "Debajo intento construir la landing completa; si algo falla, "
    "vas a ver el error detallado en lugar del mensaje genérico."
)

# =========================================================
# BLOQUE COMPLETO EN TRY/EXCEPT
# =========================================================
try:
    # ----------------------------
    # ESTILOS (muy simples)
    # ----------------------------
    st.markdown(
        """
        <style>
        .card {
            background: #ffffff;
            border: 1px solid #e0e6db;
            padding: 14px;
            border-radius: 10px;
            margin-bottom: 12px;
        }
        .btn {
            display: inline-block;
            background: #4CAF50;
            padding: 6px 12px;
            border-radius: 6px;
            color: white !important;
            text-decoration: none;
            font-weight: 600;
        }
        .center {
            text-align: center;
        }
        h1, h2, h3 {
            color: #2e5e2d;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ----------------------------
    # SELECTOR DE IDIOMA
    # ----------------------------
    if "lang" not in st.session_state:
        st.session_state.lang = "es"

    col_es, col_en = st.columns(2)
    with col_es:
        if st.button("🇦🇷 Español"):
            st.session_state.lang = "es"
    with col_en:
        if st.button("🇺🇸 English"):
            st.session_state.lang = "en"

    LANG = st.session_state.lang

    # ----------------------------
    # DICCIONARIO DE TEXTOS
    # ----------------------------
    T = {
        "es": {
            "title": "📊 PREDWEEM – Modelos Predictivos de Emergencia",
            "subtitle": "Herramientas para la gestión sustentable en la región pampeana",
            "intro": (
                "Este portal reúne modelos de emergencia desarrollados por la UNS y el INTA. "
                "Cargue datos meteorológicos o utilice los provistos automáticamente para obtener "
                "emergencia diaria y emergencia acumulada (2025)."
            ),
            "models": "Modelos disponibles",
            "guide": "Guía de uso",
            "team": "Equipo",
            "inst": "Instituciones",
            "contact": "Consultas o contacto",
            "open": "Abrir app",
        },
        "en": {
            "title": "📊 PREDWEEM – Predictive Weed Emergence Models",
            "subtitle": "Decision tools for sustainable management in the Pampas region",
            "intro": (
                "This portal contains weed emergence models developed by UNS & INTA. "
                "Upload weather data or use automatic sources to obtain daily and cumulative "
                "emergence (2025)."
            ),
            "models": "Available models",
            "guide": "User guide",
            "team": "Team",
            "inst": "Institutions",
            "contact": "Contact",
            "open": "Open app",
        },
    }

    def tr(key: str) -> str:
        return T.get(LANG, T["es"]).get(key, key)

    # -----------------------------------------------------
    # PORTADA
    # -----------------------------------------------------
    st.markdown(f"## {tr('title')}")
    st.markdown(f"#### {tr('subtitle')}")
    st.write(tr("intro"))

    # La imagen NO es obligatoria; si no está, no debería romper.
    # Si no tenés 'austral.png' en el repo, simplemente comentá esta línea.
    try:
        st.image("austral.png", width=400)
    except Exception as e_img:
        st.info("No se pudo cargar 'austral.png' (esto no detiene la app).")
        st.exception(e_img)

    # -----------------------------------------------------
    # MODELOS
    # -----------------------------------------------------
    st.markdown(f"### {tr('models')}")

    models = [
        ("Lolium sp. BORDENAVE–2025", "lolium.jpeg",
         "https://appemergenciapy-lscuxqt2j3sa9yjrwgyqnh.streamlit.app/"),
        ("Lolium sp. TRES ARROYOS–2025", "lolium.jpeg",
         "https://appemergenciapy-pfj3sr8shtoqcucopfmkat.streamlit.app/"),
        ("Avena fatua BORDENAVE–2025", "AVEFA.jpg",
         "https://appemergenciapy-mp6o4yjxbxctoekktcradc.streamlit.app/"),
        ("Hirshfeldia incana BORDENAVE–2025", "hirsin.png",
         "https://u2tod53cwpaeqmlqpmp2of.streamlit.app/"),
        ("Euphorbia davidii BORDENAVE–2025", "EUPHO.jpg",
         "https://appemergenciaapppy-gfda7txzhpsf2ahkcmv7h5.streamlit.app/"),
        ("Euphorbia davidii BAHÍA BLANCA–2025", "EUPHO.jpg",
         "https://appemergenciaapppy-ah6c82sgacq2d7z2i5uptl.streamlit.app/"),
        ("Euphorbia davidii OLAVARRÍA–2025", "EUPHO.jpg",
         "https://appemergenciaapppy-v3dns5cft6ws9p9jdhzepj.streamlit.app/"),
    ]

    for i in range(0, len(models), 3):
        cols = st.columns(3)
        for col, (name, img, url) in zip(cols, models[i:i+3]):
            with col:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                # Imagen protegida en try/except
                try:
                    st.image(img, use_column_width=True)
                except Exception:
                    st.write("(imagen no disponible)")
                st.markdown(f"**{name}**")
                st.markdown(
                    f'<a class="btn" target="_blank" href="{url}">{tr("open")}</a>',
                    unsafe_allow_html=True,
                )
                st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------------------------------
    # GUÍA DE USO
    # -----------------------------------------------------
    st.markdown(f"### {tr('guide')}")
    st.write(
        "- Formato de archivo: Excel (.xlsx)\n"
        "- Columnas requeridas: `Julian_days`, `TMAX`, `TMIN`, `Prec`\n"
        "- Salidas: EMERREL diaria y EMERAC acumulada, con fecha calendario."
    )

    for img_name in ["pipa.png", "ac.png"]:
        try:
            st.image(img_name, width=400)
        except Exception:
            st.write(f"(No se pudo cargar {img_name}, opcional)")

    # -----------------------------------------------------
    # EQUIPO
    # -----------------------------------------------------
    st.markdown(f"### {tr('team')}")

    cols_team = st.columns(5)
    team_imgs = [
        ("FOTO.jpg", "Ing. Agr. (Dr.) Guillermo R. Chantre"),
        ("Luis.JPG", "Ing. Agr. (Dr.) Luis M. Carretto"),
        ("ramon.jpeg", "Ing. Agr. Ramón Gigon"),
        ("mario.jpeg", "Ing. Agr. (MSc.) Mario R. Vigna"),
        ("fede.jpg", "Ing. Agr. (MSc.) Federico Nuñez-Fré"),
    ]

    for col, (img, caption) in zip(cols_team, team_imgs):
        with col:
            try:
                col.image(img, caption=caption)
            except Exception:
                col.write(caption)

    # -----------------------------------------------------
    # INSTITUCIONES
    # -----------------------------------------------------
    st.markdown(f"### {tr('inst')}")
    cols_inst = st.columns(4)
    inst_imgs = ["descarga.jpg", "cerzos.jpg", "inta.png", "BCP_3-100.jpg"]
    for col, img in zip(cols_inst, inst_imgs):
        with col:
            try:
                col.image(img)
            except Exception:
                col.write(img)

    # -----------------------------------------------------
    # CONTACTO
    # -----------------------------------------------------
    st.markdown(f"### {tr('contact')}")

    with st.form("contact_form"):
        name_input = st.text_input("Nombre / Name")
        email_input = st.text_input("Email")
        msg_input = st.text_area("Mensaje / Message")

        submitted = st.form_submit_button("Enviar")
        if submitted:
            # Acá en el futuro se puede conectar a Formspree o email
            st.success("Mensaje enviado (dummy). Gracias por contactarte.")

    # -----------------------------------------------------
    # FOOTER
    # -----------------------------------------------------
    st.markdown(
        """
        <div class="center" style="margin-top: 30px; color: #5b6b5b;">
        © 2025 PREDWEEM · Todos los derechos reservados.
        </div>
        """,
        unsafe_allow_html=True,
    )

except Exception as e:
    st.error("❌ Ocurrió un error al construir la landing PREDWEEM.")
    st.write("Copiá el mensaje de error que aparece abajo y pegalo en el chat para que lo podamos corregir puntualmente:")
    st.exception(e)

import streamlit as st

# Estilos personalizados
st.markdown(
    """
    <style>
    .desarrollado {
        text-align: left;
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .file-uploader {
        text-align: left;
        font-size: 14px;
    }
    .stFileUploader label {
        font-size: 14px !important;
    }
    .stFileUploader div {
        font-size: 14px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.title("Conversor de Preguntas para Blackboard Ultra")

# Información del desarrollador alineado a la izquierda
st.markdown('<div class="desarrollado">Desarrollado por: Maycoll Gamarra Chura</div>', unsafe_allow_html=True)

# Sección de carga de archivos
st.markdown("📂 **Arrastra o selecciona un archivo Excel**")

archivo = st.file_uploader("", type=["xlsx"], label_visibility="collapsed")

# Mostrar mensaje de éxito si se carga un archivo
if archivo:
    st.success("Archivo cargado correctamente.")

# Mostrar la fecha de última actualización
st.markdown("### Última actualización: **16/03/25**")

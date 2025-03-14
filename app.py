import streamlit as st

# Estilos personalizados
st.markdown(
    """
    <style>
    .desarrollado {
        text-align: left;
        font-size: 14px;
        font-weight: bold;
    }
    .stFileUploader {
        text-align: left;
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
st.markdown("📂 Arrastra o selecciona un archivo Excel")
archivo = st.file_uploader("Arrastrar y soltar archivo aquí", type=["xlsx"])

# Botón para explorar archivos
if archivo:
    st.success("Archivo cargado correctamente.")

# Mostrar la fecha de última actualización
st.markdown("### Última actualización: **16/03/25**")

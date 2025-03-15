import streamlit as st
import pandas as pd
from io import BytesIO

# Estilos personalizados
st.markdown(
    """
    <style>
    .desarrollado {
        text-align: left;
        font-size: 16px;
        font-weight: normal;
        margin-bottom: 10px;
    }
    .ultima-actualizacion {
        font-size: 12px;
        color: #555;
        margin-top: 20px;
    }
    div[data-testid="stFileUploadDropzone"] button {
        background-color: #004A98 !important;
        color: white !important;
        border: none !important;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        transition: 0.3s ease-in-out;
    }
    div[data-testid="stFileUploadDropzone"] button:hover {
        background-color: #003366 !important;
        box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.title("Conversor de Preguntas para Blackboard Ultra")

# Información del desarrollador SIN negrita
st.markdown('<div class="desarrollado">Desarrollado por: Maycoll Gamarra Chura</div>', unsafe_allow_html=True)

# Sección de carga de archivos
st.markdown("\U0001F4C2 **Arrastra o selecciona un archivo Excel**")
archivo = st.file_uploader("", type=["xlsx"], label_visibility="collapsed")

# Función para convertir el archivo Excel a formato TXT

def convertir_a_txt(archivo):
    df = pd.read_excel(archivo, sheet_name="Formato")
    
    # Simulación de conversión
    contenido_txt = "".join(df.astype(str).apply(lambda x: " ".join(x), axis=1))
    
    return contenido_txt

# Procesamiento del archivo
if archivo:
    st.success("Archivo cargado correctamente.")
    
    contenido_txt = convertir_a_txt(archivo)
    
    # Convertir el contenido a un archivo descargable
    buffer = BytesIO()
    buffer.write(contenido_txt.encode())
    buffer.seek(0)
    
    # Botón de descarga
    st.download_button(
        label="📥 Descargar archivo TXT",
        data=buffer,
        file_name="preguntas_blackboard.txt",
        mime="text/plain"
    )

# Mostrar la fecha de última actualización sin icono de enlace
st.markdown('<p class="ultima-actualizacion">Última actualización: 16/03/25</p>', unsafe_allow_html=True)

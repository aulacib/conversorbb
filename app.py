import streamlit as st
import pandas as pd
import convertir
import io

# Estilos personalizados
st.markdown(
    """
    <style>
    .titulo {
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        white-space: nowrap;
    }
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
    .block-container {
        padding-left: 5rem !important;
        padding-right: 5rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.markdown('<div class="titulo">Conversor de Preguntas para Blackboard Ultra</div>', unsafe_allow_html=True)

# Información del desarrollador
st.markdown('<div class="desarrollado">Desarrollado por: Maycoll Gamarra Chura</div>', unsafe_allow_html=True)

# Sección de carga de archivos
st.markdown("📂 **Arrastra o selecciona un archivo Excel**")
archivo = st.file_uploader("", type=["xlsx"], label_visibility="collapsed")

# Procesamiento del archivo cargado
if archivo:
    st.success("Archivo cargado correctamente.")
    df = pd.ExcelFile(archivo)
    nombre_archivo = archivo.name.replace(".xlsx", "")
    
    # Convertir preguntas a formato TXT
    texto_convertido = convertir.convertir_a_txt(df)
    
    # Generar archivo descargable
    nombre_txt = f"preguntas_{nombre_archivo}.txt"
    archivo_txt = io.BytesIO()
    archivo_txt.write(texto_convertido.encode("utf-8"))
    archivo_txt.seek(0)
    
    st.download_button(
        label="📥 Descargar archivo convertido",
        data=archivo_txt,
        file_name=nombre_txt,
        mime="text/plain"
    )

# Mostrar la fecha de última actualización
st.markdown('<p class="ultima-actualizacion">Última actualización: 16/03/25</p>', unsafe_allow_html=True)

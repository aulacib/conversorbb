import streamlit as st
import pandas as pd
import io
from convertir import convertir_excel_a_preguntas

# Estilos personalizados con mayor prioridad
st.markdown(
    """
    <style>
    /* Ajustar el margen superior de todo el contenido */
    .block-container {
        padding-top: 13px !important; /* Baja todo 7 píxeles */
    }

    /* Estilo del título con prioridad */
    h1.titulo {
        font-size: 18px !important; /* Tamaño del título más pequeño con prioridad */
        font-weight: bold;
        text-align: left;
        margin-bottom: 10px;
        color: #333;
    }

    /* Información del desarrollador */
    .desarrollado {
        text-align: left;
        font-size: 14px;
        font-weight: normal;
        margin-bottom: 10px;
        color: #444;
    }

    /* Última actualización */
    .ultima-actualizacion {
        font-size: 12px;
        color: #555;
        margin-top: 20px;
    }

    /* Estilos para el botón de subida de archivos */
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

# Título con nuevo estilo
st.markdown('<h1 class="titulo">Conversor de Preguntas para Blackboard Ultra</h1>', unsafe_allow_html=True)

# Información del desarrollador
st.markdown('<div class="desarrollado">Desarrollado por: Maycoll Gamarra Chura</div>', unsafe_allow_html=True)

# Sección de carga de archivos
st.markdown("📂 **Arrastra o selecciona un archivo Excel**")
archivo = st.file_uploader("", type=["xlsx"], label_visibility="collapsed")

if archivo:
    st.success("Archivo cargado correctamente.")
    
    # Convertir el archivo cargado
    preguntas_formateadas = convertir_excel_a_preguntas(archivo)
    
    if preguntas_formateadas:
        contenido_txt = "\n\n".join(preguntas_formateadas)
        archivo_txt = io.BytesIO()
        archivo_txt.write(contenido_txt.encode("utf-8"))
        archivo_txt.seek(0)
        
        st.download_button(
            label="📥 Descargar archivo TXT",
            data=archivo_txt,
            file_name=f"preguntas_{archivo.name.replace('.xlsx', '')}.txt",
            mime="text/plain"
        )
    else:
        st.error("No se pudieron procesar las preguntas. Verifique el archivo.")

# Fecha de última actualización
st.markdown('<p class="ultima-actualizacion">Última actualización: 16/03/25</p>', unsafe_allow_html=True)

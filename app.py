import streamlit as st
import pandas as pd
import io
from convertir import convertir_excel_a_preguntas

# Estilos personalizados
st.markdown(
    """
    <style>
    .titulo {
        font-size: 22px; /* Tamaño reducido */
        font-weight: bold;
        text-align: center;
        margin-top: 7px; /* Ajuste para que no lo tape la barra */
        margin-bottom: 10px;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título con tamaño reducido
st.markdown('<h1 class="titulo">Conversor de Preguntas para Blackboard Ultra</h1>', unsafe_allow_html=True)

# Sección de carga de archivos
archivo = st.file_uploader("Sube tu archivo Excel", type=["xlsx"])

if archivo:
    preguntas_formateadas = convertir_excel_a_preguntas(archivo)
    
    if preguntas_formateadas:
        contenido_txt = "\n\n".join(preguntas_formateadas)
        archivo_txt = io.BytesIO()
        archivo_txt.write(contenido_txt.encode("utf-8"))
        archivo_txt.seek(0)
        
        st.download_button(
            label="📥 Descargar archivo TXT",
            data=archivo_txt,
            file_name="preguntas.txt",
            mime="text/plain"
        )
    else:
        st.error("No se pudieron procesar las preguntas. Verifique el archivo.")

import streamlit as st
import pandas as pd
from io import StringIO

# Importamos la función desde convertir.py
from convertir import convertir_excel_a_preguntas

st.title("Conversor de Preguntas para Blackboard Ultra")
st.markdown("Desarrollado por: Maycoll Gamarra Chura")

st.markdown("📂 **Arrastra o selecciona un archivo Excel**")
archivo = st.file_uploader("", type=["xlsx"], label_visibility="collapsed")

if archivo:
    try:
        # Guardamos temporalmente el archivo
        df = pd.ExcelFile(archivo, engine="openpyxl")
        
        # Convertimos el archivo usando la función de convertir.py
        preguntas_txt = convertir_excel_a_preguntas(archivo)
        
        if preguntas_txt:
            contenido_txt = "\n".join(preguntas_txt)
            
            # Botón para descargar el archivo TXT
            st.download_button(
                label="Descargar archivo TXT",
                data=contenido_txt,
                file_name="preguntas_blackboard.txt",
                mime="text/plain"
            )
        else:
            st.error("No se encontraron preguntas en el archivo. Verifica que tenga el formato correcto.")
    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")

st.markdown("Última actualización: 16/03/25")

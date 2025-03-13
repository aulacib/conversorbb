import streamlit as st
import pandas as pd
import convertir  # Importa tu script de conversión
import os

st.title("Conversor de Preguntas para Blackboard Ultra")

# Subir archivo Excel
archivo_subido = st.file_uploader("Sube un archivo Excel", type=["xlsx"])

if archivo_subido is not None:
    st.write("📂 Archivo cargado:", archivo_subido.name)
    
    # Guardar temporalmente el archivo
    ruta_temporal = "archivo_temporal.xlsx"
    with open(ruta_temporal, "wb") as f:
        f.write(archivo_subido.getbuffer())

    # Convertir preguntas
    preguntas = convertir.convertir_excel_a_preguntas(ruta_temporal)

    if preguntas:
        # Guardar en TXT
        ruta_salida = "preguntas.txt"
        convertir.guardar_preguntas_en_txt(preguntas, ruta_salida)

        # Mostrar botón de descarga
        with open(ruta_salida, "rb") as f:
            st.download_button("📥 Descargar archivo TXT", f, file_name="preguntas.txt", mime="text/plain")
    else:
        st.error("❌ Hubo un error en la conversión. Revisa el formato del archivo.")

    # Borrar archivos temporales
    os.remove(ruta_temporal)
    if os.path.exists(ruta_salida):
        os.remove(ruta_salida)


import streamlit as st
import pandas as pd
import convertir  # Importa tu script de conversión
import os

st.title("Conversor de Preguntas para Blackboard Ultra")

# Subir archivo Excel
archivo_subido = st.file_uploader("📂 Sube un archivo Excel", type=["xlsx"])

if archivo_subido is not None:
    st.success("Archivo cargado correctamente.")
    
    # Guardar temporalmente el archivo
    ruta_temporal = "archivo_temporal.xlsx"
    with open(ruta_temporal, "wb") as f:
        f.write(archivo_subido.getbuffer())
    
    # Convertir preguntas
    preguntas = convertir.convertir_excel_a_preguntas(ruta_temporal)
    
    if preguntas:
        # Generar el nombre del archivo de salida
        nombre_salida = f"preguntas_{archivo_subido.name.replace('.xlsx', '')}.txt"
        
        # Guardar en TXT automáticamente
        convertir.guardar_preguntas_en_txt(preguntas, nombre_salida)
        st.success(f"Archivo guardado automáticamente en: {nombre_salida}")
    else:
        st.error("❌ Hubo un error en la conversión. Revisa el formato del archivo.")
    
    # Borrar archivo temporal
    os.remove(ruta_temporal)

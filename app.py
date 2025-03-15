import streamlit as st
import pandas as pd
import convertir  # Importa tu script de conversión
import os
import time

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
        # Crear nombre de archivo basado en el Excel subido
        nombre_archivo_txt = f"preguntas_{archivo_subido.name.replace('.xlsx', '')}.txt"
        ruta_salida = nombre_archivo_txt
        convertir.guardar_preguntas_en_txt(preguntas, ruta_salida)

        # Mostrar enlace de descarga automática en HTML
        with open(ruta_salida, "rb") as f:
            contenido_txt = f.read()
        
        time.sleep(1)  # Pequeña pausa para asegurar la generación del archivo

        href = f'<a href="data:file/txt;base64,{contenido_txt.decode("utf-8")}" download="{nombre_archivo_txt}">🔽 Descargar automáticamente</a>'
        st.markdown(href, unsafe_allow_html=True)

    else:
        st.error("❌ Hubo un error en la conversión. Revisa el formato del archivo.")

    # Borrar archivos temporales
    os.remove(ruta_temporal)
    if os.path.exists(ruta_salida):
        os.remove(ruta_salida)

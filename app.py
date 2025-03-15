import streamlit as st
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
        # Crear el nombre del archivo TXT basado en el nombre del Excel
        nombre_base = os.path.splitext(archivo_subido.name)[0]  # Elimina la extensión .xlsx
        ruta_salida = f"preguntas_{nombre_base}.txt"
        
        # Guardar automáticamente en el servidor
        convertir.guardar_preguntas_en_txt(preguntas, ruta_salida)
        
        st.success(f"✅ Archivo guardado automáticamente en: {os.path.abspath(ruta_salida)}")
    else:
        st.error("❌ Hubo un error en la conversión. Revisa el formato del archivo.")

    # Borrar archivo temporal
    os.remove(ruta_temporal)

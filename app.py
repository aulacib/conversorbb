import streamlit as st
import pandas as pd
import convertir  # Importa tu script de conversión
import os

st.title("Conversor de preguntas Blackboard Ultra")

st.markdown("<p style='text-align:center; font-size:14px;'>Desarrollado por: Maycoll Gamarra Chura</p>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; font-size:14px;'>Última actualización: 15/03/25</p>", unsafe_allow_html=True)

# Subir archivo Excel
archivo_subido = st.file_uploader("📂 Arrastra o selecciona un archivo Excel", type=["xlsx"], label_visibility='collapsed')

if archivo_subido is not None:
    st.markdown(f"<p style='color:green; font-weight:bold;'>📂 Archivo cargado: {archivo_subido.name}</p>", unsafe_allow_html=True)
    
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

        # Mostrar mensaje de éxito con fondo verde
        st.markdown("""
        <div style='background-color:#DFF2BF; padding:10px; border-radius:5px;'>
            ✅ <span style='color:green;'>Archivo cargado correctamente.</span>
        </div>
        """, unsafe_allow_html=True)

        # Mostrar botón de descarga
        with open(ruta_salida, "rb") as f:
            st.download_button("📥 Descargar archivo TXT", f, file_name="preguntas.txt", mime="text/plain")
    else:
        st.error("❌ Hubo un error en la conversión. Revisa el formato del archivo.")

    # Borrar archivos temporales
    os.remove(ruta_temporal)
    if os.path.exists(ruta_salida):
        os.remove(ruta_salida)

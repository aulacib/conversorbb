import streamlit as st
import pandas as pd
import base64
import io

def convertir_a_txt(df, nombre_archivo):
    output = io.StringIO()
    for index, row in df.iterrows():
        output.write(f"{row['Pregunta']}\n")
        for opcion in ['A', 'B', 'C', 'D']:
            if pd.notna(row[opcion]):
                output.write(f"{opcion.lower()}. {row[opcion]}\n")
        output.write("\n")
    contenido = output.getvalue()
    output.close()
    return contenido

def generar_link_descarga(contenido, nombre_archivo):
    b64 = base64.b64encode(contenido.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{nombre_archivo}">📥 Descargar archivo TXT automáticamente</a>'

# Configuración de la página
st.set_page_config(page_title="Blackboard Ultra", layout="centered")
st.markdown("""
    <h1 style="text-align: center;">Blackboard Ultra</h1>
    <p style="text-align: center;">Desarrollado por: Maycoll Gamarra Chura</p>
    <hr>
    <h3>📂 Arrastra o selecciona un archivo Excel</h3>
""", unsafe_allow_html=True)

archivo = st.file_uploader("Drag and drop file here", type=["xlsx"], help="Limit 200MB per file • XLSX")

if archivo is not None:
    df = pd.read_excel(archivo, sheet_name="Formato")
    nombre_archivo = archivo.name.replace(".xlsx", ".txt")
    contenido_txt = convertir_a_txt(df, nombre_archivo)
    
    st.success("Archivo cargado correctamente.")
    st.markdown(generar_link_descarga(contenido_txt, nombre_archivo), unsafe_allow_html=True)
    
    # Guardar en buffer para la descarga manual
    buffer = io.BytesIO()
    buffer.write(contenido_txt.encode())
    buffer.seek(0)
    st.download_button(label="Descargar archivo TXT", data=buffer, file_name=nombre_archivo, mime="text/plain")

st.markdown("<p style='text-align: center;'>Última actualización: 16/03/25</p>", unsafe_allow_html=True)

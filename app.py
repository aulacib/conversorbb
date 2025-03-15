import streamlit as st
import pandas as pd
import base64
from io import BytesIO

def convertir_a_txt(df, nombre_archivo):
    output = BytesIO()
    for index, row in df.iterrows():
        output.write(f"{row['Pregunta']}\n".encode())
        if 'Opciones' in df.columns:
            opciones = row['Opciones'].split(';')
            for i, opcion in enumerate(opciones):
                output.write(f"{chr(97 + i)}. {opcion}\n".encode())
        output.write(b"\n")
    output.seek(0)
    b64 = base64.b64encode(output.read()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{nombre_archivo}.txt">\ud83d\udd0d Descargar archivo TXT</a>'
    return href

st.markdown("# Blackboard Ultra", unsafe_allow_html=True)
st.markdown("Desarrollado por: Maycoll Gamarra Chura")
st.markdown("### \ud83d\udcc2 Arrastra o selecciona un archivo Excel")

archivo = st.file_uploader("", type=["xlsx"], help="Limit 200MB per file • XLSX")
if archivo:
    df = pd.read_excel(archivo)
    nombre_archivo = archivo.name.replace(".xlsx", "")
    st.success("Archivo cargado correctamente.")
    st.markdown(convertir_a_txt(df, nombre_archivo), unsafe_allow_html=True)
    st.markdown("Última actualización: 16/03/25")

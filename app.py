import streamlit as st
import pandas as pd
import io

def convertir_a_txt(df):
    output = io.StringIO()
    for index, row in df.iterrows():
        output.write(f"{row['Pregunta']}\n")
        opciones = ['A', 'B', 'C', 'D', 'E']
        for i, opcion in enumerate(opciones):
            if pd.notna(row.get(opcion)):
                output.write(f"{opcion}. {row[opcion]}\n")
        output.write(f"Respuesta correcta: {row['Respuesta']}\n\n")
    return output.getvalue()

st.title("Conversor de Preguntas para Blackboard Ultra")
st.write("Desarrollado por: Maycoll Gamarra Chura")

uploaded_file = st.file_uploader("Arrastra o selecciona un archivo Excel", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file, sheet_name='Formato')
        txt_data = convertir_a_txt(df)
        st.success("Archivo cargado correctamente.")
        st.download_button(
            label="Descargar automáticamente",
            data=txt_data,
            file_name="preguntas_blackboard.txt",
            mime="text/plain",
            key="auto_download"
        )
    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")

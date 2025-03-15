import streamlit as st
import pandas as pd

def convertir_excel_a_txt(archivo):
    df = pd.read_excel(archivo, sheet_name="Formato")
    
    # Procesar el archivo según el formato esperado
    preguntas_txt = []
    
    for _, row in df.iterrows():
        tipo_pregunta = str(row.get("Tipo de Pregunta", "")).strip().lower()
        enunciado = str(row.get("Pregunta", "")).strip()
        
        if tipo_pregunta == "opción múltiple":
            preguntas_txt.append(f"MC\t{enunciado}")
            opciones = ["A", "B", "C", "D"]
            for i, opcion in enumerate(opciones):
                respuesta = str(row.get(opcion, "")).strip()
                if respuesta:
                    preguntas_txt.append(f"{opcion}. {respuesta}")
            preguntas_txt.append("")  # Línea en blanco entre preguntas
        
        elif tipo_pregunta == "verdadero/falso":
            preguntas_txt.append(f"TF\t{enunciado}")
            respuesta_correcta = str(row.get("Respuesta Correcta", "")).strip()
            preguntas_txt.append(f"Correcta: {respuesta_correcta}")
            preguntas_txt.append("")  # Línea en blanco
        
        elif tipo_pregunta == "rellenar el espacio en blanco":
            preguntas_txt.append(f"blank 1. {enunciado}")
            respuestas_correctas = str(row.get("I", "")).strip()
            if respuestas_correctas:
                preguntas_txt.append(f"a. {respuestas_correctas}")
            preguntas_txt.append("")  # Línea en blanco

    return "\n".join(preguntas_txt)

# Interfaz en Streamlit
st.title("Conversor de Preguntas para Blackboard Ultra")

# Información del desarrollador (sin negrita)
st.markdown("Desarrollado por: Maycoll Gamarra Chura")

st.markdown("📂 **Arrastra o selecciona un archivo Excel**")
archivo = st.file_uploader("", type=["xlsx"], label_visibility="collapsed")

if archivo:
    st.success("Archivo cargado correctamente.")

    # Convertir el archivo Excel a TXT
    contenido_txt = convertir_excel_a_txt(archivo)

    # Botón para descargar el archivo TXT
    st.download_button(
        label="Descargar archivo TXT",
        data=contenido_txt,
        file_name="preguntas_blackboard.txt",
        mime="text/plain"
    )

st.markdown("Última actualización: 16/03/25")

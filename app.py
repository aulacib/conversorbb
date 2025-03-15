import streamlit as st
import pandas as pd
import os

def convertir_excel_a_txt(archivo, nombre_salida):
    df = pd.read_excel(archivo, sheet_name="Formato")
    
    preguntas_txt = []
    
    for _, row in df.iterrows():
        tipo_pregunta = str(row.get("Tipo de Pregunta", "")).strip().lower()
        enunciado = str(row.get("Enunciado", "")).strip()
        
        if tipo_pregunta == "opción múltiple":
            preguntas_txt.append(f"MC\t{enunciado}")
            opciones = ["A", "B", "C", "D"]
            for opcion in opciones:
                respuesta = str(row.get(opcion, "")).strip()
                if respuesta:
                    preguntas_txt.append(f"{opcion}. {respuesta}")
            preguntas_txt.append("")  
        
        elif tipo_pregunta == "verdadero/falso":
            preguntas_txt.append(f"TF\t{enunciado}")
            respuesta_correcta = str(row.get("Respuesta Correcta", "")).strip()
            preguntas_txt.append(f"Correcta: {respuesta_correcta}")
            preguntas_txt.append("")  
        
        elif tipo_pregunta == "rellenar el espacio en blanco":
            preguntas_txt.append(f"blank 1. {enunciado}")
            respuestas_correctas = str(row.get("I", "")).strip()
            if respuestas_correctas:
                preguntas_txt.append(f"a. {respuestas_correctas}")
            preguntas_txt.append("")  
    
    ruta_salida = os.path.join(os.getcwd(), nombre_salida)
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write("\n".join(preguntas_txt))
    
    return ruta_salida

# Interfaz en Streamlit
st.title("Conversor de Preguntas para Blackboard Ultra")
st.markdown("Desarrollado por: Maycoll Gamarra Chura")
st.markdown("📂 **Arrastra o selecciona un archivo Excel**")

archivo = st.file_uploader("", type=["xlsx"], label_visibility="collapsed")

if archivo:
    st.success("Archivo cargado correctamente.")
    nombre_salida = "preguntas_blackboard.txt"
    ruta_archivo_txt = convertir_excel_a_txt(archivo, nombre_salida)
    st.success(f"Archivo guardado automáticamente en: {ruta_archivo_txt}")

st.markdown("Última actualización: 16/03/25")

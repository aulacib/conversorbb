import streamlit as st
import pandas as pd
import io

def convertir_excel_a_txt(archivo):
    try:
        # Leer el archivo Excel
        xls = pd.ExcelFile(archivo)
        
        # Verificar si la hoja "Formato" existe
        if "Formato" not in xls.sheet_names:
            return None, "Error: La hoja 'Formato' no existe en el archivo."

        df = pd.read_excel(xls, sheet_name="Formato")

        # Validar que la columna "Pregunta" existe
        if "Pregunta" not in df.columns:
            return None, "Error: La columna 'Pregunta' no se encontró en el archivo."

        preguntas_txt = []
        
        for _, row in df.iterrows():
            tipo_pregunta = str(row.get("Tipo de Pregunta", "") or "").strip().lower()
            enunciado = str(row.get("Pregunta", "") or "").strip()
            
            if not enunciado:
                continue  # Saltar filas sin pregunta

            if tipo_pregunta == "opción múltiple":
                preguntas_txt.append(f"MC\t{enunciado}")
                opciones = ["A", "B", "C", "D"]
                for opcion in opciones:
                    respuesta = str(row.get(opcion, "") or "").strip()
                    if respuesta:
                        preguntas_txt.append(f"{opcion}. {respuesta}")
                preguntas_txt.append("")  # Línea en blanco entre preguntas
            
            elif tipo_pregunta == "verdadero/falso":
                preguntas_txt.append(f"TF\t{enunciado}")
                respuesta_correcta = str(row.get("Respuesta Correcta", "") or "").strip()
                preguntas_txt.append(f"Correcta: {respuesta_correcta}")
                preguntas_txt.append("")  # Línea en blanco
            
            elif tipo_pregunta == "rellenar el espacio en blanco":
                preguntas_txt.append(f"blank 1. {enunciado}")
                respuestas_correctas = str(row.get("I", "") or "").strip()
                if respuestas_correctas:
                    preguntas_txt.append(f"a. {respuestas_correctas}")
                preguntas_txt.append("")  # Línea en blanco

        return "\n".join(preguntas_txt), None  # Retorna contenido y sin errores

    except Exception as e:
        return None, f"Error al procesar el archivo: {str(e)}"

# Interfaz en Streamlit
st.title("Conversor de Preguntas para Blackboard Ultra")

st.markdown("Desarrollado por: Maycoll Gamarra Chura")
st.markdown("📂 **Arrastra o selecciona un archivo Excel**")
archivo = st.file_uploader("", type=["xlsx"], label_visibility="collapsed")

if archivo:
    contenido_txt, error = convertir_excel_a_txt(archivo)

    if error:
        st.error(error)
    else:
        st.success("Archivo procesado correctamente. La descarga ha comenzado automáticamente.")

        # Convertir a archivo de texto y descargar automáticamente
        txt_bytes = io.BytesIO(contenido_txt.encode("utf-8"))
        st.download_button(
            label="Descargar archivo TXT",
            data=txt_bytes,
            file_name="preguntas_blackboard.txt",
            mime="text/plain"
        )

st.markdown("Última actualización: 16/03/25")

import streamlit as st
import pandas as pd
import convertir  # Importa tu script de conversión
import os

# Agregar estilos personalizados con CSS
st.markdown(
    """
    <style>
        /* Personalizar el cuadro de carga de archivos */
        div[data-testid="stFileUploader"] {
            border: 2px dashed #2E86C1; /* Borde azul con líneas discontinuas */
            padding: 20px;
            border-radius: 10px;
            transition: all 0.3s ease-in-out; /* Efecto suave */
        }

        /* Efecto al pasar el mouse (hover) */
        div[data-testid="stFileUploader"]:hover {
            background-color: #EAF2F8; /* Fondo celeste al pasar el mouse */
            border: 2px solid #1F618D; /* Borde sólido azul oscuro */
            box-shadow: 0px 0px 10px rgba(46, 134, 193, 0.5); /* Sombra azul */
        }

        /* Personalizar el texto del label */
        div[data-testid="stFileUploader"] > label {
            font-size: 18px;
            font-weight: bold;
            color: #1F618D;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Conversor de Preguntas para Blackboard Ultra")

# Subir archivo Excel
archivo_subido = st.file_uploader("📂 Arrastra o selecciona un archivo Excel", type=["xlsx"])

if archivo_subido is not None:
    st.write("📂 Archivo cargado:", archivo_subido.name)
    
    # Guardar temporalmente el archivo
    ruta_temporal = "archivo_temporal.xlsx"
    with open(ruta_temporal, "wb") as f:
        f.write(archivo_subido.getbuffer())

    # Obtener el nombre base del archivo sin la extensión
    nombre_base = os.path.splitext(archivo_subido.name)[0]

    # Convertir preguntas
    preguntas = convertir.convertir_excel_a_preguntas(ruta_temporal)

    if preguntas:
        # Guardar en TXT con el nombre correcto
        ruta_salida = f"preguntas_{nombre_base}.txt"
        convertir.guardar_preguntas_en_txt(preguntas, ruta_salida)

        # Mostrar botón de descarga con el nombre correcto
        with open(ruta_salida, "rb") as f:
            st.download_button("📥 Descargar archivo TXT", f, file_name=ruta_salida, mime="text/plain")
    else:
        st.error("❌ Hubo un error en la conversión. Revisa el formato del archivo.")

    # Borrar archivos temporales
    os.remove(ruta_temporal)
    if os.path.exists(ruta_salida):
        os.remove(ruta_salida)


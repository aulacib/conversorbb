import streamlit as st
import pandas as pd
import io
from convertir import convertir_excel_a_preguntas

# Estilos personalizados
st.markdown(
    """
    <style>
    .desarrollado {
        text-align: left;
        font-size: 16px;
        font-weight: normal; /* Se quita la negrita */
        margin-bottom: 10px;
    }
    .ultima-actualizacion {
        font-size: 12px;
        color: #555;
        margin-top: 20px;
    }
    /* Estilos para el botón de subida de archivos */
    div[data-testid="stFileUploadDropzone"] button {
        background-color: #004A98 !important; /* Azul Cibertec */
        color: white !important;
        border: none !important;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        transition: 0.3s ease-in-out;
    }
    div[data-testid="stFileUploadDropzone"] button:hover {
        background-color: #003366 !important; /* Azul más oscuro al pasar el mouse */
        box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.title("Conversor de Preguntas para Blackboard Ultra")

# Información del desarrollador SIN negrita
st.markdown('<div class="desarrollado">Desarrollado por: Maycoll Gamarra Chura</div>', unsafe_allow_html=True)

# Sección de carga de archivos
st.markdown("📂 **Arrastra o selecciona un archivo Excel**")
archivo = st.file_uploader("", type=["xlsx"], label_visibility="collapsed")

if archivo:
    st.success("Archivo cargado correctamente.")
    
    # Convertir el archivo cargado
    preguntas_formateadas = convertir_excel_a_preguntas(archivo)
    
    if preguntas_formateadas:
        contenido_txt = "\n\n".join(preguntas_formateadas)
        archivo_txt = io.BytesIO()
        archivo_txt.write(contenido_txt.encode("utf-8"))
        archivo_txt.seek(0)
        
        st.download_button(
            label="📥 Descargar archivo TXT",
            data=archivo_txt,
            file_name=f"preguntas_{archivo.name.replace('.xlsx', '')}.txt",
            mime="text/plain"
        )
    else:
        st.error("No se pudieron procesar las preguntas. Verifique el archivo.")

# Mostrar la fecha de última actualización sin icono de enlace
st.markdown('<p class="ultima-actualizacion">Última actualización: 16/03/25</p>', unsafe_allow_html=True)

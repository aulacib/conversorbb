import streamlit as st
import pandas as pd
import convertir  # Importa tu script de conversión
import os

# Estilos personalizados para centrar los elementos
st.markdown("""
    <style>
        .titulo {
            font-size: 36px;
            font-weight: bold;
            text-align: left;
        }
        .desarrollador {
            font-size: 16px;
            color: #666;
            text-align: left;
        }
        .archivo-cargado {
            color: green;
            font-weight: bold;
        }
        .footer {
            font-size: 14px;
            color: #666;
            margin-top: 20px;
        }
        .boton-descarga {
            display: flex;
            justify-content: left;
        }
    </style>
""", unsafe_allow_html=True)

# Título y desarrollador
st.markdown('<div class="titulo">Blackboard Ultra</div>', unsafe_allow_html=True)
st.markdown('<div class="desarrollador">Desarrollado por: Maycoll Gamarra Chura</div>', unsafe_allow_html=True)

# Subir archivo Excel
archivo_subido = st.file_uploader("📂 Arrastra o selecciona un archivo Excel", type=["xlsx"])

if archivo_subido is not None:
    st.write(f"📂 **Archivo cargado:** {archivo_subido.name}")
    
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

        # Mostrar botón de descarga
        with open(ruta_salida, "rb") as f:
            st.markdown('<div class="boton-descarga">', unsafe_allow_html=True)
            st.download_button("📥 Descargar archivo TXT", f, file_name="preguntas.txt", mime="text/plain")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("❌ Hubo un error en la conversión. Revisa el formato del archivo.")

    # Borrar archivos temporales
    os.remove(ruta_temporal)
    if os.path.exists(ruta_salida):
        os.remove(ruta_salida)

# Última actualización
st.markdown('<div class="footer">Última actualización: 15/03/25</div>', unsafe_allow_html=True)

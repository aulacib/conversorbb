import streamlit as st
import pandas as pd
import io
from convertir import convertir_excel_a_preguntas

# Estilos personalizados
st.markdown(
    """
    <style>
    /* Ajustar solo la posición del título */
    .titulo {
        font-size: 24px; /* Reducido */
        font-weight: bold;
        text-align: left;
        margin-top: 7px; /* Baja solo el título 7px */
        margin-bottom: 10px;
        color: #333;
    }

    /* Información del desarrollador */
    .desarrollado {
        text-align: left;
        font-size: 14px;
        font-weight: normal;
        margin-bottom: 10px;
        color: #444;
    }

    /* Última actualización */
   

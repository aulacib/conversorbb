import pandas as pd
import os

def convertir_excel_a_preguntas(ruta_archivo):
    # Cargar todas las hojas del archivo
    xls = pd.ExcelFile(ruta_archivo, engine="openpyxl")
    
    # Verificar si la hoja "Formato" existe
    if "Formato" not in xls.sheet_names:
        print(f"Error: No se encontró la hoja 'Formato' en el archivo {ruta_archivo}.")
        return None
    
    # Leer solo la hoja "Formato"
    df = pd.read_excel(xls, sheet_name="Formato", dtype=str)
    
    # Buscar la fila donde están los encabezados correctos
    encabezados_correctos = ["N° Pregunta", "Enunciado", "Alternativas", "Detalle de Alternativas", "Marcar la alternativa correcta"]
    fila_encabezados = None
    
    for i, fila in df.iterrows():
        if all(col in fila.values for col in encabezados_correctos):
            fila_encabezados = i
            break
    
    if fila_encabezados is None:
        print(f"Error: No se encontraron los encabezados correctos en la hoja 'Formato' del archivo {ruta_archivo}.")
        return None
    
    # Leer solo desde la fila donde están los encabezados correctos
    df = pd.read_excel(xls, sheet_name="Formato", skiprows=fila_encabezados+1, dtype=str)
    
    # Verificar que las columnas requeridas están en el DataFrame
    for columna in encabezados_correctos:
        if columna not in df.columns:
            print(f"Error: Falta la columna '{columna}' en el archivo {ruta_archivo}.")
            return None
    
    preguntas_formateadas = []
    
    pregunta_actual = None
    enunciado_actual = ""
    opciones = []
    
    for _, fila in df.iterrows():
        if not pd.isna(fila["N° Pregunta"]):  # Nueva pregunta detectada
            if pregunta_actual is not None and opciones:  # Si hay una pregunta previa con opciones, guardarla
                preguntas_formateadas.append(f"{pregunta_actual}. {enunciado_actual}\n" + "\n".join(opciones))
            
            pregunta_actual = int(fila["N° Pregunta"])
            enunciado_actual = str(fila["Enunciado"]).strip()
            opciones = []  # Reiniciar opciones
        
        letra = str(fila["Alternativas"]).strip()
        detalle = str(fila["Detalle de Alternativas"]).strip()
        correcta = str(fila["Marcar la alternativa correcta"]).strip()
        
        # Asegurar que no se impriman valores vacíos o "nan"
        if detalle.lower() not in ["nan", "", "none"]:
            # Reemplazar True/False por Verdadero/Falso si es necesario
            if detalle.upper() == "TRUE":
                detalle = "VERDADERO"
            elif detalle.upper() == "FALSE":
                detalle = "FALSO"
            
            if correcta.upper() == "X":
                opciones.append(f"*{letra}) {detalle}")
            else:
                opciones.append(f"{letra}) {detalle}")
    
    if pregunta_actual is not None and opciones:  # Agregar la última pregunta si tiene opciones
        preguntas_formateadas.append(f"{pregunta_actual}. {enunciado_actual}\n" + "\n".join(opciones))
    
    return preguntas_formateadas

def guardar_preguntas_en_txt(preguntas, ruta_salida):
    with open(ruta_salida, "w", encoding="utf-8") as f:
        for pregunta in preguntas:
            f.write(pregunta + "\n\n")

if __name__ == "__main__":
    carpeta_origen = "C:/ScriptsPython/origen"
    carpeta_procesados = "C:/ScriptsPython/procesados"
    os.makedirs(carpeta_procesados, exist_ok=True)
    
    archivos_excel = [f for f in os.listdir(carpeta_origen) if f.endswith(".xlsx")]
    
    for archivo in archivos_excel:
        ruta_archivo = os.path.join(carpeta_origen, archivo)
        nombre_base = os.path.splitext(archivo)[0]  # Obtener el nombre sin la extensión
        
        preguntas = convertir_excel_a_preguntas(ruta_archivo)
        if preguntas:
            ruta_salida = os.path.join(carpeta_procesados, f"preguntas_{nombre_base}.txt")
            guardar_preguntas_en_txt(preguntas, ruta_salida)
            print(f"Preguntas guardadas en {ruta_salida}")

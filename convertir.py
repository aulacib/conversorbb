import pandas as pd
import os

def convertir_excel_a_preguntas(ruta_archivo):
    xls = pd.ExcelFile(ruta_archivo, engine="openpyxl")

    if "Formato" not in xls.sheet_names:
        print(f"Error: No se encontró la hoja 'Formato' en el archivo {ruta_archivo}.")
        return None

    df = pd.read_excel(xls, sheet_name="Formato", dtype=str)

    encabezados_correctos = ["N° Pregunta", "Enunciado", "Alternativas", "Detalle de Alternativas", "Marcar la alternativa correcta", "Tipo"]
    fila_encabezados = None

    for i, fila in df.iterrows():
        if all(col in fila.values for col in encabezados_correctos):
            fila_encabezados = i
            break

    if fila_encabezados is None:
        print(f"Error: No se encontraron los encabezados correctos en el archivo {ruta_archivo}.")
        return None

    df = pd.read_excel(xls, sheet_name="Formato", skiprows=fila_encabezados+1, dtype=str)

    for columna in encabezados_correctos:
        if columna not in df.columns:
            print(f"Error: Falta la columna '{columna}' en el archivo {ruta_archivo}.")
            return None

    preguntas_formateadas = []
    pregunta_actual = None
    enunciado_actual = ""
    tipo_pregunta = ""
    respuesta_correcta = None
    alternativas = []

    for _, fila in df.iterrows():
        if not pd.isna(fila["N° Pregunta"]):  
            if pregunta_actual is not None:
                if tipo_pregunta == "Verdadero/Falso":
                    preguntas_formateadas.append(f"{pregunta_actual}. {enunciado_actual}\n{respuesta_correcta}")
                elif tipo_pregunta in ["Opción Múltiple", "Respuesta Múltiple"]:
                    preguntas_formateadas.append(f"{pregunta_actual}. {enunciado_actual}\n" + "\n".join(alternativas))
                elif tipo_pregunta == "Rellenar el espacio en blanco":
                    preguntas_formateadas.append(f"blank {pregunta_actual}. {enunciado_actual}\n" + "\n".join(alternativas))
                elif tipo_pregunta == "Emparejamiento":
                    preguntas_formateadas.append(f"match {pregunta_actual}. {enunciado_actual}\n" + "\n".join(alternativas))

            pregunta_actual = int(fila["N° Pregunta"])
            enunciado_actual = str(fila["Enunciado"]).strip()
            tipo_pregunta = str(fila["Tipo"]).strip()
            respuesta_correcta = "No definida"
            alternativas = []

        alternativa = str(fila["Alternativas"]).strip().lower()
        detalle = str(fila["Detalle de Alternativas"]).strip()
        correcta = str(fila["Marcar la alternativa correcta"]).strip().upper()

        if tipo_pregunta == "Verdadero/Falso":
            if correcta == "X":
                if alternativa == "a":
                    respuesta_correcta = "TRUE"
                elif alternativa == "b":
                    respuesta_correcta = "FALSE"
        
        elif tipo_pregunta in ["Opción Múltiple", "Respuesta Múltiple"]:
            letra_opcion = chr(97 + len(alternativas)) + ") "  # Generar letras a, b, c, d...
            if correcta == "X":
                alternativas.append(f"*{letra_opcion}{detalle}")
            else:
                alternativas.append(f"{letra_opcion}{detalle}")

        elif tipo_pregunta == "Rellenar el espacio en blanco":
            letra_opcion = chr(97 + len(alternativas)) + ". "  # Generar letras a, b, c, d...
            alternativas.append(f"{letra_opcion}{detalle}")

        elif tipo_pregunta == "Emparejamiento":
            letra_opcion = chr(97 + len(alternativas)) + ") "  # Generar letras a, b, c, d...
            alternativas.append(f"{letra_opcion}{detalle}")

    if pregunta_actual is not None:
        if tipo_pregunta == "Verdadero/Falso":
            preguntas_formateadas.append(f"{pregunta_actual}. {enunciado_actual}\n{respuesta_correcta}")
        elif tipo_pregunta in ["Opción Múltiple", "Respuesta Múltiple"]:
            preguntas_formateadas.append(f"{pregunta_actual}. {enunciado_actual}\n" + "\n".join(alternativas))
        elif tipo_pregunta == "Rellenar el espacio en blanco":
            preguntas_formateadas.append(f"blank {pregunta_actual}. {enunciado_actual}\n" + "\n".join(alternativas))
        elif tipo_pregunta == "Emparejamiento":
            preguntas_formateadas.append(f"match {pregunta_actual}. {enunciado_actual}\n" + "\n".join(alternativas))

    if not preguntas_formateadas:
        print("No se encontraron preguntas para exportar.")

    return preguntas_formateadas

def guardar_preguntas_en_txt(preguntas, ruta_salida):
    if preguntas:
        with open(ruta_salida, "w", encoding="utf-8") as f:
            for pregunta in preguntas:
                f.write(pregunta + "\n\n")
        print(f"Preguntas guardadas en {ruta_salida}")
    else:
        print("No hay preguntas para guardar.")

if __name__ == "__main__":
    carpeta_origen = "C:/ScriptsPython/origen"
    carpeta_procesados = "C:/ScriptsPython/procesados"
    os.makedirs(carpeta_procesados, exist_ok=True)

    archivos_excel = [f for f in os.listdir(carpeta_origen) if f.endswith(".xlsx")]

    for archivo in archivos_excel:
        ruta_archivo = os.path.join(carpeta_origen, archivo)
        nombre_base = os.path.splitext(archivo)[0]  

        preguntas = convertir_excel_a_preguntas(ruta_archivo)
        if preguntas:
            ruta_salida = os.path.join(carpeta_procesados, f"preguntas_{nombre_base}.txt")
            guardar_preguntas_en_txt(preguntas, ruta_salida)
        else:
            print(f"No se generaron preguntas para el archivo {archivo}.")

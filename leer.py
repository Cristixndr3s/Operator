import pandas as pd

archivo_excel="tareas.xlsx"

try:
    # Leer el archivo Excel
    df = pd.read_excel(archivo_excel)

    # Mostrar las primeras filas para verificar que se lee correctamente
    print("✅ Archivo leído correctamente. Vista previa:")
    print(df.head())  # Muestra las primeras 5 filas
except Exception as e:
    print(f"❌ Error al leer el archivo: {e}")
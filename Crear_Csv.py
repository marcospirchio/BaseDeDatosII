import pandas as pd
from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["basket_db"]
jugadores = db["jugadores"]

# Obtener los datos de MongoDB y convertirlos en una lista
data = list(jugadores.find({}, {"_id": 0}))  # Excluir el _id para evitar problemas con el CSV

# Verificar si hay datos antes de exportar
if data:
    # Convertir los datos a un DataFrame de Pandas
    df = pd.DataFrame(data)

    # Exportar a CSV
    df.to_csv("jugadores_exportados.csv", index=False, encoding="utf-8")

    print("Datos exportados correctamente a 'jugadores_exportados.csv'.")

    # Mostrar las primeras filas del archivo exportado
    print("\nVista previa de los datos exportados:")
    print(df.head())  # mostramos algunas filas del dataframe
else:
    print("No hay datos en la colección 'jugadores', no se exportó ningún archivo.")

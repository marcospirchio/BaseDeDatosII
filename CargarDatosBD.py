from pymongo import MongoClient
import json

# Conectar a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["basket_db"]
jugadores = db["jugadores"]

with open("TemaSeleccionadoPorElGrupo.json") as file:
    data = json.load(file)
    jugadores.insert_many(data)
print("Datos cargados correctamente")
from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Base de datos y colección
db = client["basket_db"]
jugadores = db["jugadores"]

jugadores.delete_many({})
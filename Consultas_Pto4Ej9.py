from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["basket_db"]
jugadores = db["jugadores"]

# 1 Listar jugadores mayores de 30 años con más de 1000 partidos jugados
print("\nJugadores mayores de 30 años con más de 1000 partidos jugados:")
resultado = list(jugadores.find({"edad": {"$gt": 30}, "partidos_jugados": {"$gt": 700}}))
if resultado:
    for jugador in resultado:
        print(jugador)
else:
    print("No hay jugadores que cumplan con estos criterios.")

# 2 Contar cuántos jugadores hay por equipo
print("\nCantidad de jugadores por equipo:")
pipeline = [{"$group": {"_id": "$equipo", "total_jugadores": {"$sum": 1}}}]
resultado = list(jugadores.aggregate(pipeline))
if resultado:
    for item in resultado:
        print(item)
else:
    print("No hay jugadores registrados en la base de datos.")

# 3 Obtener el promedio de puntos anotados por equipo
print("\nPromedio de puntos anotados por equipo:")
pipeline = [
    {"$group": {"_id": "$equipo", "promedio_puntos": {"$avg": "$puntos_anotados"}}}
]
resultado = list(jugadores.aggregate(pipeline))
if resultado:
    for item in resultado:
        item["promedio_puntos"] = round(item["promedio_puntos"], 2)
        print(item)
else:
    print("No hay datos suficientes para calcular el promedio de puntos.")

# 4 Listar los 10 jugadores con más puntos anotados
print("\nTop 10 jugadores con más puntos anotados con al menos 100 partidos jugados:")
resultado = list(jugadores.find({"partidos_jugados": {"$gte": 100}}).sort("puntos_anotados", -1).limit(10))
if resultado:
    for jugador in resultado:
        print(jugador)
else:
    print("No hay jugadores con al menos 100 partidos jugados.")

# 5 Contar cuántos jugadores tienen más de 500 partidos jugados
cantidad = jugadores.count_documents({"partidos_jugados": {"$gt": 500}, "puntos_anotados": {"$gte": 10}})
if cantidad > 0:
    print(f"\nCantidad de jugadores con más de 500 partidos jugados y al menos 10 puntos de promedio: {cantidad}")
else:
    print("\nNo hay jugadores que cumplan con estos criterios.")

print("\nConsultas completadas.")

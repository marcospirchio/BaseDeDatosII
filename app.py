from flask import Flask, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# Conectar a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["basket_db"]
jugadores = db["jugadores"]

@app.route('/', methods=['GET'])
def home():
    return jsonify({"mensaje": "Bienvenido a la API de Jugadores de la NBA. Usa /jugadores para ver la lista."})


# Ruta para obtener todos los jugadores
@app.route('/jugadores', methods=['GET'])
def get_jugadores():
    jugadores_list = list(jugadores.find({}, {"_id": 0}))  # Excluir _id para evitar problemas en JSON
    if jugadores_list:
        return jsonify(jugadores_list), 200
    else:
        return jsonify({"mensaje": "No hay jugadores en la base de datos"}), 404

# Ruta para obtener un jugador por nombre
@app.route('/jugadores/<nombre>', methods=['GET'])
def get_jugador(nombre):
    jugador = jugadores.find_one({"nombre": nombre}, {"_id": 0})
    if jugador:
        return jsonify(jugador), 200
    else:
        return jsonify({"mensaje": f"No se encontró un jugador con el nombre {nombre}"}), 404

# Ruta para obtener los 10 jugadores con más puntos anotados
@app.route('/jugadores/top10', methods=['GET'])
def get_top10_jugadores():
    top_jugadores = list(jugadores.find({"partidos_jugados": {"$gte": 100}})
                          .sort("puntos_anotados", -1)
                          .limit(10))

    # Convertir ObjectId a string para evitar errores de serialización
    for jugador in top_jugadores:
        jugador["_id"] = str(jugador["_id"])

    if top_jugadores:
        return jsonify(top_jugadores), 200
    else:
        return jsonify({"mensaje": "No hay suficientes jugadores para generar un ranking"}), 404

# Ruta para obtener el promedio de puntos anotados por equipo
@app.route('/jugadores/promedio_puntos', methods=['GET'])
def get_promedio_puntos():
    pipeline = [
        {"$group": {"_id": "$equipo", "promedio_puntos": {"$avg": "$puntos_anotados"}}}
    ]
    promedio_puntos = list(jugadores.aggregate(pipeline))
    if promedio_puntos:
        # Redondear los valores del promedio a 2 decimales
        for item in promedio_puntos:
            item["promedio_puntos"] = round(item["promedio_puntos"], 2)
        return jsonify(promedio_puntos), 200
    else:
        return jsonify({"mensaje": "No hay datos suficientes para calcular los promedios"}), 404

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
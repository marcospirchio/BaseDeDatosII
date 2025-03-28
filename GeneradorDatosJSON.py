from pymongo import MongoClient
from faker import Faker
import random
import json

# Conectar a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["basket_db"]
jugadores = db["jugadores"]

# Instanciamos Faker
fake = Faker()

# Genera 50 jugadores ficticios
datos = []
for _ in range(50):
    jugador = {
        "nombre": fake.first_name(),
        "apellido": fake.last_name(),
        "equipo": random.choice([
            "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls",
            "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets", "Detroit Pistons", "Golden State Warriors",
            "Houston Rockets", "Indiana Pacers", "Los Angeles Clippers", "Los Angeles Lakers", "Memphis Grizzlies",
            "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks",
            "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns", "Portland Trail Blazers",
            "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", "Utah Jazz", "Washington Wizards"
        ]),
        "edad": random.randint(18, 40),
        "nro_camiseta": random.randint(0, 99),
        "puntos_anotados": round(random.uniform(10, 35), 1),
        "partidos_jugados": random.randint(10, 1200)
    }
    datos.append(jugador)

# Guardar en archivo JSON
with open("TemaSeleccionadoPorElGrupo.json", "w") as file:
    json.dump(datos, file, indent=4)

print("Archivo JSON generado exitosamente.")

from pymongo import MongoClient

# Conexion a MongoDB
client = MongoClient("mongodb://localhost:27017/")

# lista de bases de datos disponibles
databases = client.list_database_names()

print("Bases de datos disponibles:")
for db in databases:
    print(f"- {db}")

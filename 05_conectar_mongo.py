import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("No se encontró MONGO_URI en el archivo .env")

cliente = MongoClient(MONGO_URI)
print(cliente.admin.command("ping"))
print("Conexión exitosa con MongoDB Atlas")

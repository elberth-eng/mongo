import os
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

cliente = MongoClient(os.getenv("MONGO_URI"))
db = cliente["empresa_ventas"]

df = pd.read_excel("ventas_limpias.xlsx")
df["Fecha"] = pd.to_datetime(df["Fecha"])

registros = df.to_dict(orient="records")

for registro in registros:
    registro["Fecha"] = registro["Fecha"].to_pydatetime()


for nombre in ["ventas", "datos_analisis"]:
    coleccion = db[nombre]
    coleccion.delete_many({})
    resultado = coleccion.insert_many([dict(r) for r in registros])
    print(f"Documentos insertados en {nombre}: {len(resultado.inserted_ids)}")

print("Base de datos:", db.name)

cliente.close()

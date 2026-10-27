import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

cliente = MongoClient(os.getenv("MONGO_URI"))
db = cliente["empresa_ventas"]
coleccion = db["datos_analisis"]

print("Total de documentos:", coleccion.count_documents({}))

documentos = list(coleccion.find({}, {"_id": 0}))
df = pd.DataFrame(documentos)
print(df.head())

ventas_categoria = (
    df.groupby("Categoria")["Total_Venta"]
    .sum()
    .sort_values(ascending=False)
)
print("\nVentas por categoría:")
print(ventas_categoria)

plt.figure(figsize=(8, 5))
ventas_categoria.plot(kind="bar", color="seagreen")
plt.title("Ventas por categoría - datos desde MongoDB Atlas")
plt.xlabel("Categoría")
plt.ylabel("Importe vendido")
plt.tight_layout()
plt.savefig("mongo_ventas_categoria.png", dpi=300)
plt.show()


consulta = coleccion.find(
    {"Total_Venta": {"$gt": 5000}},
    {"_id": 0, "Fecha": 1, "Producto": 1, "Total_Venta": 1}
).sort("Total_Venta", -1)

df_filtrado = pd.DataFrame(list(consulta))
print("\nVentas mayores a 5000:")
print(df_filtrado)


pipeline = [
    {"$group": {
        "_id": "$Categoria",
        "Total": {"$sum": "$Total_Venta"},
        "Operaciones": {"$sum": 1},
    }},
    {"$sort": {"Total": -1}},
]
print("\nAgrupación por categoría (aggregate):")
for doc in coleccion.aggregate(pipeline):
    print(doc)

cliente.close()

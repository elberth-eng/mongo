import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("ventas_limpias.xlsx")
df["Fecha"] = pd.to_datetime(df["Fecha"])

ventas_categoria = df.groupby("Categoria")["Total_Venta"].sum().sort_values()

plt.figure(figsize=(8, 5))
ventas_categoria.plot(kind="barh", color="steelblue")
plt.title("Ventas totales por categoría")
plt.xlabel("Importe vendido")
plt.ylabel("Categoría")
plt.tight_layout()
plt.savefig("ventas_por_categoria.png", dpi=300)
plt.show()


ventas_mes = df.groupby("Mes")["Total_Venta"].sum()

plt.figure(figsize=(8, 5))
plt.plot(ventas_mes.index, ventas_mes.values, marker="o", color="darkgreen")
plt.title("Tendencia mensual de ventas")
plt.xlabel("Mes")
plt.ylabel("Importe vendido")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("ventas_por_mes.png", dpi=300)
plt.show()

top_productos = (
    df.groupby("Producto")["Total_Venta"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

plt.figure(figsize=(8, 5))
plt.bar(top_productos.index, top_productos.values, color="indianred")
plt.title("Top 5 productos por ingreso")
plt.xlabel("Producto")
plt.ylabel("Importe vendido")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("top_productos.png", dpi=300)
plt.show()


ventas_vendedor = df.groupby("Vendedor")["Total_Venta"].sum()

plt.figure(figsize=(6, 6))
plt.pie(
    ventas_vendedor.values,
    labels=ventas_vendedor.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Participación de cada vendedor")
plt.tight_layout()
plt.savefig("participacion_vendedores.png", dpi=300)
plt.show()

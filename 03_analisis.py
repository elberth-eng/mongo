import pandas as pd

df = pd.read_excel("ventas_limpias.xlsx")
df["Fecha"] = pd.to_datetime(df["Fecha"])

print("=== Resumen general ===")
print("Total de registros:", len(df))
print("Ingreso total:", df["Total_Venta"].sum())
print("Ticket promedio:", df["Total_Venta"].mean())
print("Venta máxima:", df["Total_Venta"].max())
print("Venta mínima:", df["Total_Venta"].min())

ventas_producto = (
    df.groupby("Producto", as_index=False)["Total_Venta"]
    .sum()
    .sort_values("Total_Venta", ascending=False)
)
print("\n=== Ventas por producto ===")
print(ventas_producto)

ventas_categoria = (
    df.groupby("Categoria", as_index=False)["Total_Venta"]
    .sum()
    .sort_values("Total_Venta", ascending=False)
)
print("\n=== Ventas por categoría ===")
print(ventas_categoria)

ventas_vendedor = (
    df.groupby("Vendedor", as_index=False)
    .agg(Total_Ventas=("Total_Venta", "sum"),
         Unidades=("Cantidad", "sum"),
         Operaciones=("Total_Venta", "count"))
    .sort_values("Total_Ventas", ascending=False)
)
print("\n=== Ventas por vendedor ===")
print(ventas_vendedor)

ventas_mes = (
    df.groupby("Mes", as_index=False)["Total_Venta"]
    .sum()
    .sort_values("Mes")
)
print("\n=== Ventas por mes ===")
print(ventas_mes)

producto_top = (
    df.groupby("Producto")["Cantidad"]
    .sum()
    .sort_values(ascending=False)
    .head(1)
)
print("\n=== Producto más vendido por unidades ===")
print(producto_top)

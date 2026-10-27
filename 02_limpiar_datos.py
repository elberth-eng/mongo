import pandas as pd

df = pd.read_excel("ventas.xlsx", sheet_name="Ventas")

print("Valores nulos:")
print(df.isnull().sum())
print("Filas duplicadas:", df.duplicated().sum())

df = df.dropna(how="all")
df = df.drop_duplicates()

df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")
df["Cantidad"] = pd.to_numeric(df["Cantidad"], errors="coerce")
df["Precio_Unitario"] = pd.to_numeric(df["Precio_Unitario"], errors="coerce")

df = df.dropna(subset=["Fecha", "Producto", "Cantidad", "Precio_Unitario"])

df["Total_Venta"] = df["Cantidad"] * df["Precio_Unitario"]
df["Anio"] = df["Fecha"].dt.year
df["Mes"] = df["Fecha"].dt.month

print(df.head())
print(df.info())
print("Registros tras limpieza:", len(df))

df.to_excel("ventas_limpias.xlsx", index=False)

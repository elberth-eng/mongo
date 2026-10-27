import pandas as pd

df = pd.read_excel("ventas.xlsx", sheet_name="Ventas")

print(df.head(10))
print("Dimensiones:", df.shape)
print(df.info())
print(df.describe())

import random
from datetime import date, timedelta
import pandas as pd

random.seed(42)

productos = {
    "Laptop": ("Computo", 14500),
    "Monitor": ("Computo", 3800),
    "Impresora": ("Computo", 4200),
    "Tablet": ("Computo", 6500),
    "Mouse": ("Accesorios", 350),
    "Teclado": ("Accesorios", 650),
    "Audifonos": ("Accesorios", 900),
    "USB 64GB": ("Accesorios", 220),
    "Silla Gamer": ("Mobiliario", 5200),
    "Escritorio": ("Mobiliario", 3900),
}
vendedores = ["Ana", "Luis", "Maria", "Carlos"]

filas = []
inicio = date(2026, 1, 5)
for i in range(40):
    producto = random.choice(list(productos))
    categoria, precio = productos[producto]
    cantidad = random.randint(1, 4) if precio > 3000 else random.randint(5, 20)
    filas.append({
        "Fecha": pd.Timestamp(inicio + timedelta(days=i * 4 + random.randint(0, 3))),
        "Producto": producto,
        "Categoria": categoria,
        "Cantidad": cantidad,
        "Precio_Unitario": precio,
        "Vendedor": random.choice(vendedores),
    })

df = pd.DataFrame(filas)


df = pd.concat([df, df.iloc[[3]], pd.DataFrame([{}])], ignore_index=True)

df.to_excel("ventas.xlsx", sheet_name="Ventas", index=False)
print("ventas.xlsx creado con", len(df), "filas")

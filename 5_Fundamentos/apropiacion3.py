import csv

# Datos de ejemplo
ventas = [
    ["codigo", "producto", "cantidad"],
    ["001", "Manzana", 3],
    ["002", "Pera", 5],
    ["001", "Manzana", 2],
    ["003", "Banano", 4],   
    ["002", "Pera", 1],
    ["004", "Fresa", 6],
    ["001", "Manzana", 5]
]

# Crear el archivo CSV con todos los registros
with open("ventas.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(ventas)

print("Archivo ventas.csv creado correctamente ✅")

codigos_productos = set()  # conjunto de códigos únicos
frecuencia = {}  # diccionario de producto -> total vendido

# Leer el archivo
with open("ventas.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        codigo = fila["codigo"]
        producto = fila["producto"]
        cantidad = int(fila["cantidad"])  # 👈 convertir a número

        # agregar el código al conjunto (no se repite)
        codigos_productos.add(codigo)

        # acumular ventas por producto
        if producto in frecuencia:
            frecuencia[producto] += cantidad
        else:
            frecuencia[producto] = cantidad

# Mostrar resultados
print("\n📦 Conjunto de productos vendidos:")
print(codigos_productos)

print("\n🏆 Productos más vendidos:")
producto_ordeando = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)

for producto, cantidad in producto_ordeando:
    print(f"{producto}: {cantidad} unidades vendidas")

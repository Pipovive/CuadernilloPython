conjunto = [("Producto A", 150),
            ("Producto B", 100), 
            ("Producto A", 150),
            ("Producto C", 180), 
            ("Producto B", 100), 
            ("Producto A", 150), 
            ("Producto D", 200), 
            ("Producto C", 150), 
            ("Producto D", 200), 
            ("Producto E", 400),
            ("Producto F", 200)]

# Crear diccionario sumando valores de productos duplicados
diccionario = {}

for producto, valor in conjunto:
    if producto in diccionario:
        diccionario[producto] += valor
    else: 
        diccionario[producto] = valor

# ===== FUNCIONES =====

def mostrar_ventas():
    """Muestra todas las ventas por producto"""
    print("\n" + "=" * 50)
    print("📊 VENTAS POR PRODUCTO")
    print("=" * 50)
    for producto, total in diccionario.items():
        print(f"  {producto}: ${total}")
    print("=" * 50)

def total_ventas():
    """Calcula el total de todas las ventas"""
    suma = 0
    for value in diccionario.values():
        suma += value
    return suma

def promedio_ventas():
    """Calcula el promedio de ventas"""
    if len(diccionario) == 0:
        return 0
    total = total_ventas()
    promedio = total / len(diccionario)
    return promedio

def max_venta():
    """Encuentra el producto con la venta máxima"""
    if not diccionario:
        return None, 0
    
    producto_max = None
    valor_max = 0
    
    for producto, valor in diccionario.items():
        if valor > valor_max:
            valor_max = valor
            producto_max = producto
    
    return producto_max, valor_max

def min_venta():
    """Encuentra el producto con la venta mínima"""
    if not diccionario:
        return None, 0
    
    producto_min = list(diccionario.keys())[0]
    valor_min = diccionario[producto_min]
    
    for producto, valor in diccionario.items():
        if valor < valor_min:
            valor_min = valor
            producto_min = producto
    
    return producto_min, valor_min

def agregar_venta():
    """Agrega una nueva venta"""
    print("\n--- AGREGAR NUEVA VENTA ---")
    producto = input("Nombre del producto: ").strip()
    
    if not producto:
        print("❌ El nombre no puede estar vacío")
        return
    
    try:
        valor = int(input("Valor de la venta: $"))
        
        if producto in diccionario:
            diccionario[producto] += valor
            print(f"✓ Se agregó ${valor} a {producto}")
        else:
            diccionario[producto] = valor
            print(f"✓ Nuevo producto '{producto}' agregado con ${valor}")
    except ValueError:
        print("❌ El valor debe ser un número")

def eliminar_producto():
    """Elimina un producto del diccionario"""
    print("\n--- ELIMINAR PRODUCTO ---")
    producto = input("Nombre del producto a eliminar: ").strip()
    
    if producto in diccionario:
        valor = diccionario[producto]
        del diccionario[producto]
        print(f"✓ Producto '{producto}' (${valor}) eliminado")
    else:
        print(f"❌ El producto '{producto}' no existe")

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 50)
    print("        SISTEMA DE ANÁLISIS DE VENTAS")
    print("=" * 50)
    print("1. Ver todas las ventas")
    print("2. Total de ventas")
    print("3. Promedio de ventas")
    print("4. Producto con mayor venta")
    print("5. Producto con menor venta")
    print("6. Análisis completo")
    print("7. Agregar nueva venta")
    print("8. Eliminar producto")
    print("9. Salir")
    print("=" * 50)

def analisis_completo():
    """Muestra un análisis completo de las ventas"""
    print("\n" + "=" * 50)
    print("📈 ANÁLISIS COMPLETO DE VENTAS")
    print("=" * 50)
    
    total = total_ventas()
    promedio = promedio_ventas()
    prod_max, val_max = max_venta()
    prod_min, val_min = min_venta()
    
    print(f"\n💰 Total de ventas: ${total}")
    print(f"📊 Promedio de ventas: ${promedio:.2f}")
    print(f"📈 Mayor venta: {prod_max} - ${val_max}")
    print(f"📉 Menor venta: {prod_min} - ${val_min}")
    print(f"🛍️  Total de productos: {len(diccionario)}")
    print("\n" + "=" * 50)

# ===== PROGRAMA PRINCIPAL =====

def main():
    print("\n¡Bienvenido al Sistema de Análisis de Ventas!")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\nSelecciona una opción (1-9): "))
        except ValueError:
            print("\n❌ Por favor ingresa un número válido")
            continue
        
        if opcion == 1:
            mostrar_ventas()
            
        elif opcion == 2:
            total = total_ventas()
            print(f"\n💰 Total de ventas: ${total}")
            
        elif opcion == 3:
            promedio = promedio_ventas()
            print(f"\n📊 Promedio de ventas: ${promedio:.2f}")
            
        elif opcion == 4:
            prod_max, val_max = max_venta()
            print(f"\n📈 Producto con MAYOR venta: {prod_max} - ${val_max}")
            
        elif opcion == 5:
            prod_min, val_min = min_venta()
            print(f"\n📉 Producto con MENOR venta: {prod_min} - ${val_min}")
            
        elif opcion == 6:
            analisis_completo()
            
        elif opcion == 7:
            agregar_venta()
            
        elif opcion == 8:
            eliminar_producto()
            
        elif opcion == 9:
            print("\n¡Gracias por usar el sistema! 👋")
            break
            
        else:
            print("\n❌ Opción no válida. Elige entre 1 y 9")

# Ejecutar el programa
if __name__ == "__main__":
    main()
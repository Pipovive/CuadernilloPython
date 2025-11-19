# Diccionario de inventario: clave = nombre del producto, valor = {"cantidad": X, "precio": Y}
inventario = {
    "Laptop": {"cantidad": 15, "precio": 2500000},
    "Mouse": {"cantidad": 50, "precio": 35000},
    "Teclado": {"cantidad": 30, "precio": 120000},
    "Monitor": {"cantidad": 20, "precio": 800000},
    "Audífonos": {"cantidad": 40, "precio": 85000},
    "Webcam": {"cantidad": 25, "precio": 150000},
    "Micrófono": {"cantidad": 18, "precio": 200000},
    "Impresora": {"cantidad": 12, "precio": 450000},
    "Tablet": {"cantidad": 22, "precio": 1200000},
    "Cargador": {"cantidad": 60, "precio": 45000}
}

# ===== FUNCIONES =====

def mostrar_inventario():
    """Muestra todo el inventario con sus detalles"""
    if not inventario:
        print("\n⚠ El inventario está vacío")
        return
    
    print("\n" + "=" * 70)
    print("📦 INVENTARIO COMPLETO")
    print("=" * 70)
    print(f"{'Producto':<20} {'Cantidad':<12} {'Precio':<15} {'Total':<15}")
    print("-" * 70)
    
    for producto, datos in inventario.items():
        cantidad = datos["cantidad"]
        precio = datos["precio"]
        total = cantidad * precio
        print(f"{producto:<20} {cantidad:<12} ${precio:<14,} ${total:,}")
    
    print("=" * 70)

def calcular_precio_total_inventario():
    """Calcula el precio total de todo el inventario"""
    total = 0
    
    for producto, datos in inventario.items():
        cantidad = datos["cantidad"]
        precio = datos["precio"]
        total += cantidad * precio
    
    return total

def mostrar_precio_total():
    """Muestra el precio total del inventario"""
    total = calcular_precio_total_inventario()
    
    print("\n" + "=" * 70)
    print("💰 PRECIO TOTAL DEL INVENTARIO")
    print("=" * 70)
    print(f"Valor total: ${total:,}")
    print(f"Cantidad de productos diferentes: {len(inventario)}")
    
    # Calcular cantidad total de items
    total_items = sum(datos["cantidad"] for datos in inventario.values())
    print(f"Cantidad total de items: {total_items}")
    print("=" * 70)

def buscar_producto():
    """Busca un producto por su nombre y muestra toda su información"""
    print("\n--- BUSCAR PRODUCTO ---")
    nombre = input("Nombre del producto a buscar: ").strip()
    
    if nombre in inventario:
        datos = inventario[nombre]
        cantidad = datos["cantidad"]
        precio = datos["precio"]
        total = cantidad * precio
        
        print("\n" + "=" * 70)
        print(f"📦 INFORMACIÓN DEL PRODUCTO: {nombre}")
        print("=" * 70)
        print(f"Cantidad en stock: {cantidad} unidades")
        print(f"Precio unitario: ${precio:,}")
        print(f"Valor total en inventario: ${total:,}")
        print("=" * 70)
    else:
        print(f"\n❌ El producto '{nombre}' no existe en el inventario")

def actualizar_precio():
    """Actualiza el precio de un producto existente"""
    print("\n--- ACTUALIZAR PRECIO ---")
    nombre = input("Nombre del producto: ").strip()
    
    if nombre not in inventario:
        print(f"\n❌ El producto '{nombre}' no existe en el inventario")
        return
    
    precio_actual = inventario[nombre]["precio"]
    print(f"Precio actual: ${precio_actual:,}")
    
    try:
        nuevo_precio = float(input("Nuevo precio: $"))
        
        if nuevo_precio < 0:
            print("❌ El precio no puede ser negativo")
            return
        
        inventario[nombre]["precio"] = nuevo_precio
        print(f"\n✓ Precio actualizado correctamente")
        print(f"  Precio anterior: ${precio_actual:,}")
        print(f"  Precio nuevo: ${nuevo_precio:,}")
    except ValueError:
        print("❌ El precio debe ser un número válido")

def agregar_producto():
    """Agrega un nuevo producto al inventario"""
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    nombre = input("Nombre del producto: ").strip()
    
    if not nombre:
        print("❌ El nombre no puede estar vacío")
        return
    
    if nombre in inventario:
        print(f"❌ El producto '{nombre}' ya existe. Usa la opción de actualizar")
        return
    
    try:
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: $"))
        
        if cantidad < 0 or precio < 0:
            print("❌ La cantidad y el precio deben ser positivos")
            return
        
        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
        print(f"\n✓ Producto '{nombre}' agregado correctamente")
    except ValueError:
        print("❌ Valores inválidos. La cantidad debe ser entero y el precio un número")

def actualizar_cantidad():
    """Actualiza la cantidad de un producto"""
    print("\n--- ACTUALIZAR CANTIDAD ---")
    nombre = input("Nombre del producto: ").strip()
    
    if nombre not in inventario:
        print(f"\n❌ El producto '{nombre}' no existe en el inventario")
        return
    
    cantidad_actual = inventario[nombre]["cantidad"]
    print(f"Cantidad actual: {cantidad_actual} unidades")
    
    try:
        nueva_cantidad = int(input("Nueva cantidad: "))
        
        if nueva_cantidad < 0:
            print("❌ La cantidad no puede ser negativa")
            return
        
        inventario[nombre]["cantidad"] = nueva_cantidad
        print(f"\n✓ Cantidad actualizada correctamente")
        print(f"  Cantidad anterior: {cantidad_actual}")
        print(f"  Cantidad nueva: {nueva_cantidad}")
    except ValueError:
        print("❌ La cantidad debe ser un número entero")

def eliminar_producto():
    """Elimina un producto del inventario"""
    print("\n--- ELIMINAR PRODUCTO ---")
    nombre = input("Nombre del producto a eliminar: ").strip()
    
    if nombre in inventario:
        datos = inventario[nombre]
        del inventario[nombre]
        print(f"\n✓ Producto '{nombre}' eliminado del inventario")
        print(f"  Cantidad eliminada: {datos['cantidad']}")
        print(f"  Precio: ${datos['precio']:,}")
    else:
        print(f"\n❌ El producto '{nombre}' no existe")

def productos_bajo_stock():
    """Muestra productos con stock bajo (menos de 20 unidades)"""
    print("\n" + "=" * 70)
    print("⚠️  PRODUCTOS CON STOCK BAJO (Menos de 20 unidades)")
    print("=" * 70)
    
    productos_bajos = {p: d for p, d in inventario.items() if d["cantidad"] < 20}
    
    if not productos_bajos:
        print("✓ Todos los productos tienen stock suficiente")
    else:
        for producto, datos in productos_bajos.items():
            print(f"{producto}: {datos['cantidad']} unidades")
    
    print("=" * 70)

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 70)
    print("              📦 SISTEMA DE GESTIÓN DE INVENTARIO 📦")
    print("=" * 70)
    print("1.  Mostrar inventario completo")
    print("2.  Mostrar precio total del inventario")
    print("3.  Buscar producto")
    print("4.  Actualizar precio de producto")
    print("5.  Actualizar cantidad de producto")
    print("6.  Agregar nuevo producto")
    print("7.  Eliminar producto")
    print("8.  Ver productos con stock bajo")
    print("9.  Salir")
    print("=" * 70)

# ===== PROGRAMA PRINCIPAL =====

def main():
    print("\n¡Bienvenido al Sistema de Gestión de Inventario!")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\nSelecciona una opción (1-9): "))
        except ValueError:
            print("\n❌ Por favor ingresa un número válido")
            continue
        
        if opcion == 1:
            mostrar_inventario()
            
        elif opcion == 2:
            mostrar_precio_total()
            
        elif opcion == 3:
            buscar_producto()
            
        elif opcion == 4:
            actualizar_precio()
            
        elif opcion == 5:
            actualizar_cantidad()
            
        elif opcion == 6:
            agregar_producto()
            
        elif opcion == 7:
            eliminar_producto()
            
        elif opcion == 8:
            productos_bajo_stock()
            
        elif opcion == 9:
            print("\n¡Gracias por usar el sistema! 📦👋")
            break
            
        else:
            print("\n❌ Opción no válida. Elige entre 1 y 9")

# Ejecutar el programa
if __name__ == "__main__":
    main()
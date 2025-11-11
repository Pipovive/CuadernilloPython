productos = {"001", "002", "003"}

while True:
    print("\n📦 SISTEMA DE INVENTARIO")
    print("1: Agregar nuevo producto")
    print("2: Buscar producto")
    print("3: Eliminar producto")
    print("4: Salir")

    try:
        d = int(input("Acción a elegir: "))
    except ValueError:
        print("⚠️ Debes digitar un número (entre 1 y 4).")
        continue

    if d == 1:
        nuevo = input("Digita el código del nuevo producto: ")
        if nuevo in productos:
            print("⚠️ Ese producto ya existe en el inventario.")
        else:
            productos.add(nuevo)
            print(f"✅ Producto {nuevo} agregado correctamente.")

    elif d == 2:
        buscar = input("Digita el código del producto a buscar: ")
        if buscar in productos:
            print(f"🔎 El producto {buscar} está disponible en el inventario.")
        else:
            print("❌ Producto no encontrado.")

    elif d == 3:
        eliminar = input("Digita el código del producto a eliminar: ")
        if eliminar in productos:
            productos.discard(eliminar)
            print(f"🗑️ Producto {eliminar} eliminado correctamente.")
        else:
            print("⚠️ Ese producto no existe en el inventario.")

    elif d == 4:
        print("👋 Saliendo del sistema...")
        break

    else:
        print("⚠️ Opción inválida. Intenta de nuevo.")

    # Mostrar la lista actualizada de productos
    print("\n📋 Inventario actual:")
    for p in productos:
        print(f"- {p}")

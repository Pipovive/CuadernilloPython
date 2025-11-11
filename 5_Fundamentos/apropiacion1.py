correos = {"juan@gmail.com", "antonia@gmail.com", "julieta@gmail.com"}

while True:
    print("\n📧 GESTOR DE EMPLEADOS")
    print("1: Insertar un nuevo empleado")
    print("2: Buscar un empleado")
    print("3: Eliminar un empleado")
    print("4: Salir")

    try:
        decision = int(input("Selecciona una opción: "))
    except ValueError:
        print("❌ Debes digitar un número (1-4).")
        continue

    if decision == 1:
        nuevo = input("Digita el correo del nuevo empleado: ")
        correos.add(nuevo)
        print("✅ Correo agregado correctamente.")

    elif decision == 2:
        buscar = input("Digita el correo a buscar: ")
        if buscar in correos:
            print(f"✅ Se encontró el correo: {buscar}")
        else:
            print("❌ Correo no encontrado.")

    elif decision == 3:
        eliminar = input("Digita el correo que quieres eliminar: ")
        if eliminar in correos:
            correos.discard(eliminar)
            print("🗑️ Correo eliminado correctamente.")
        else:
            print("⚠️ Ese correo no está en la lista.")

    elif decision == 4:
        print("👋 Programa terminado.")
        break

    else:
        print("⚠️ Opción inválida. Intenta de nuevo.")

    # Mostrar lista actualizada
    print("\nLista actual de correos:")
    for c in correos:
        print("-", c)

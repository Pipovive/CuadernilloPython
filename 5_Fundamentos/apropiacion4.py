# Sistema de control de acceso con conjuntos

empleados = {}  # Diccionario: empleado -> conjunto de permisos

while True:
    print("\n===== SISTEMA DE CONTROL DE ACCESO =====")
    print("1. Asignar permiso a empleado")
    print("2. Verificar permisos de empleado")
    print("3. Revocar permiso de empleado")
    print("4. Mostrar todos los empleados y sus permisos")
    print("5. Salir")

    try:
        opcion = int(input("Selecciona una opción: "))
    except ValueError:
        print("❌ Debes ingresar un número (1-5).")
        continue

    # 1️⃣ Asignar permisos
    if opcion == 1:
        nombre = input("Nombre del empleado: ").capitalize()
        permiso = input("Permiso a asignar (por ejemplo: 'Oficina', 'Servidor', 'Bodega'): ").capitalize()

        # Si el empleado no existe, se crea
        if nombre not in empleados:
            empleados[nombre] = set()

        empleados[nombre].add(permiso)
        print(f"✅ Permiso '{permiso}' asignado a {nombre}.")

    # 2️⃣ Verificar permisos
    elif opcion == 2:
        nombre = input("Nombre del empleado: ").capitalize()
        if nombre in empleados:
            print(f"🔐 Permisos de {nombre}: {empleados[nombre]}")
        else:
            print(f"⚠️ {nombre} no tiene permisos registrados.")

    # 3️⃣ Revocar permisos
    elif opcion == 3:
        nombre = input("Nombre del empleado: ").capitalize()
        if nombre in empleados:
            permiso = input("Permiso a revocar: ").capitalize()
            if permiso in empleados[nombre]:
                empleados[nombre].remove(permiso)
                print(f"❎ Permiso '{permiso}' revocado de {nombre}.")
            else:
                print(f"⚠️ {nombre} no tiene el permiso '{permiso}'.")
        else:
            print(f"⚠️ {nombre} no existe en el sistema.")

    # 4️⃣ Mostrar todos los empleados
    elif opcion == 4:
        if empleados:
            print("\n📋 Lista de empleados y permisos:")
            for emp, permisos in empleados.items():
                print(f"- {emp}: {', '.join(permisos)}")
        else:
            print("No hay empleados registrados aún.")

    # 5️⃣ Salir
    elif opcion == 5:
        print("👋 Saliendo del sistema...")
        break
    else:
        print("❌ Opción inválida, elige entre 1 y 5.")

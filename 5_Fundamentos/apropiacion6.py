
empleados = {
    1001:{"nombre":"Juan", "cargo": "Programador"},
    1002:{"nombre":"Julieta", "cargo": "Diseñador"},
    1003:{"nombre":"Mar", "cargo":"Gerente"},
    1004:{"nombre":"Antonia", "cargo": "Contador"},
    1005:{"nombre":"Francia", "cargo": "Recursos Humanos"}
}

def mostrar_menu(): 
    """Muestra el menú principal"""
    print("\n====SISTEMA DE GESTION DE EMPLEADOS====")
    print("1. Buscar Empleado")
    print("2. Eliminar Empleado")
    print("3. Mostrar todos los Empleado")
    print("4. Agregar Empleado")
    print("5. Buscar Empleado")
    print("=" * 40)

def buscar_empleado():
    try: 
        id_empleado = int(input("Ingresa el numero de identificacion: \n"))

        if id_empleado in empleados:
            print(f"\n--Informacion del empleado--")
            print(f"ID: {id_empleado}")
            print(f"Nombre: {empleados[id_empleado]['nombre']}")
            print(f"Cargo: {empleados[id_empleado]['cargo']}")
        else: 
            print(f"\n❌ No se encontró ningún empleado con ID {id_empleado}")
    except ValueError:
        print("\n❌ Error: Debes ingresar un número válido")

def eliminar_empleado():
    try:
        id_empleado = int(input("\nIngresa numero de identificacion: \n"))
        if id_empleado in empleados:
            nombre = empleados[id_empleado]['nombre']
            del empleados[id_empleado]
            print(f"\n El usuario con nombre {nombre} fue elimnado")
        else: 
           print(f"\n❌ No se encontró ningún empleado con ID {id_empleado}")
    except ValueError:
        print("\n❌ Error: Debes ingresar un número válido")

def mostrar_todos():
    if not empleados:
        print("No hay empleados disponibles")
    
    print("\n--- LISTA DE TODOS LOS EMPLEADOS ---")
    for key,val in empleados.items():
        print(f"\nID: {key}")
        print(f" Nombre: {val['nombre']}")
        print(f"Cargo: {val['cargo']}")

def agregar_empleado():
    """Agrega un nuevo empleado"""
    try:
        id_empleado = int(input("\nIngresa el número de identificación: "))
        
        if id_empleado in empleados:
            print(f"\n❌ Ya existe un empleado con ID {id_empleado}")
            return
        
        nombre = input("Ingresa el nombre completo: ")
        cargo = input("Ingresa el cargo: ")
        
        empleados[id_empleado] = {"nombre": nombre, "cargo": cargo}
        print(f"\n✓ Empleado {nombre} agregado correctamente")
    except ValueError:
        print("\n❌ Error: El ID debe ser un número válido")


def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-5): ")
        
        if opcion == "1":
            buscar_empleado()
        elif opcion == "2":
            eliminar_empleado()
        elif opcion == "3":
            mostrar_todos()
        elif opcion == "4":
            agregar_empleado()
        elif opcion == "5":
            print("\n¡Hasta luego! 👋")
            break
        else:
            print("\n❌ Opción no válida. Por favor selecciona una opción del 1 al 5")

# Ejecutar el programa
if __name__ == "__main__":
    main()



    
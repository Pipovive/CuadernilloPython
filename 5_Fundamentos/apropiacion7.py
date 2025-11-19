contactos_avanzados = {
    "Juan": {"telefono": "318", "correo": "juan@gmail.com", "direccion": "carrera#1"},
    "Julieta": {"telefono": "320", "correo": "julieta@gmail.com", "direccion": "carrera#2"},
    "Carlos": {"telefono": "319", "correo": "carlos@gmail.com", "direccion": "carrera#3"}
}

def mostrar_menu():
    print("\n=== MENÚ DE CONTACTOS ===")
    print("1. Mostrar Contactos")
    print("2. Buscar Contacto")
    print("3. Actualizar Contacto")
    print("4. Agregar Contacto")
    print("5. Eliminar Contacto")
    print("6. Salir")
    print("=" * 26)

def mostrar_contactos():
    if not contactos_avanzados:  # ✓ Sin paréntesis
        print("\n⚠ No tienes contactos guardados")
        return
    
    print("\n--- LISTA DE CONTACTOS ---")
    for key, val in contactos_avanzados.items():
        print(f"\n📱 Contacto: {key}")
        print(f"   Teléfono: {val['telefono']}")
        print(f"   Correo: {val['correo']}")
        print(f"   Dirección: {val['direccion']}")

def buscar_contactos(): 
    contacto_id = input("\nEscribe el nombre del contacto que vas a buscar: ").capitalize()

    if contacto_id in contactos_avanzados:  # ✓ Usar 'in' no 'is'
        print(f"\n--- Información del contacto: {contacto_id} ---")
        print(f"Teléfono: {contactos_avanzados[contacto_id]['telefono']}")
        print(f"Correo: {contactos_avanzados[contacto_id]['correo']}")
        print(f"Dirección: {contactos_avanzados[contacto_id]['direccion']}")
    else: 
        print(f"\n❌ El contacto '{contacto_id}' no existe")

def actualizar_contacto():
    contacto_id = input("\nEscribe el nombre del contacto a actualizar: ").capitalize()
    
    if contacto_id not in contactos_avanzados:
        print(f"\n❌ El contacto '{contacto_id}' no existe")
        return
    
    print(f"\n--- Actualizando contacto: {contacto_id} ---")
    print("Deja en blanco si no quieres cambiar el campo")
    
    nuevo_telefono = input(f"Nuevo teléfono (actual: {contactos_avanzados[contacto_id]['telefono']}): ")
    nuevo_correo = input(f"Nuevo correo (actual: {contactos_avanzados[contacto_id]['correo']}): ")
    nueva_direccion = input(f"Nueva dirección (actual: {contactos_avanzados[contacto_id]['direccion']}): ")
    
    if nuevo_telefono:
        contactos_avanzados[contacto_id]['telefono'] = nuevo_telefono
    if nuevo_correo:
        contactos_avanzados[contacto_id]['correo'] = nuevo_correo
    if nueva_direccion:
        contactos_avanzados[contacto_id]['direccion'] = nueva_direccion
    
    print(f"\n✓ Contacto '{contacto_id}' actualizado correctamente")

def agregar_contacto():
    nombre = input("\nNombre del nuevo contacto: ").capitalize()
    
    if nombre in contactos_avanzados:
        print(f"\n❌ El contacto '{nombre}' ya existe")
        return
    
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    direccion = input("Dirección: ")
    
    contactos_avanzados[nombre] = {
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion
    }
    
    print(f"\n✓ Contacto '{nombre}' agregado correctamente")

def eliminar_contacto():
    contacto_id = input("\nEscribe el nombre del contacto a eliminar: ").capitalize()
    
    if contacto_id in contactos_avanzados:
        del contactos_avanzados[contacto_id]
        print(f"\n✓ Contacto '{contacto_id}' eliminado correctamente")
    else:
        print(f"\n❌ El contacto '{contacto_id}' no existe")

def main():
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\nSelecciona una opción: "))
        except ValueError:
            print("\n❌ Por favor ingresa un número válido")
            continue
        
        if opcion == 1:
            mostrar_contactos()
        elif opcion == 2:
            buscar_contactos()
        elif opcion == 3:
            actualizar_contacto()
        elif opcion == 4:
            agregar_contacto()
        elif opcion == 5:
            eliminar_contacto()
        elif opcion == 6:
            print("\n¡Hasta luego! 👋")
            break
        else:
            print("\n❌ Opción no válida. Elige entre 1 y 6")

# Ejecutar el programa
if __name__ == "__main__":
    main()
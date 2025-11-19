suscriptores = set()

while True:
    print("\n========== PANEL DE SUSCRIPCIONES ==========")
    print("1: Agregar nuevo correo")
    print("2: Verificar si un usuario ya existe")
    print("3: Cancelar la suscripción de un usuario")
    print("4: Mostrar todos los suscriptores")
    print("5: Salir")
    print("=" * 44)
    
    try: 
        opcion = int(input("\n¿Qué opción eliges? "))
    except ValueError:
        print("\n❌ Digitaste un valor incorrecto. Por favor ingresa un número.")
        continue
    
    if opcion == 1: 
        correo = input("\nDigita el correo del nuevo suscriptor: ").strip().lower()
        
        if not correo:
            print("❌ El correo no puede estar vacío")
        elif correo in suscriptores: 
            print(f"❌ El correo {correo} ya está registrado")
        else:
            suscriptores.add(correo)
            print(f"✓ Correo {correo} agregado exitosamente")
            
    elif opcion == 2:
        correo = input("\nDigita el correo a buscar: ").strip().lower()
        
        if correo in suscriptores:
            print(f"✓ El correo {correo} está registrado")
        else: 
            print(f"❌ El correo {correo} todavía no se ha registrado")
            
    elif opcion == 3:
        correo = input("\nEscribe el correo que vas a cancelar: ").strip().lower()
        
        if correo in suscriptores:
            suscriptores.discard(correo)
            print(f"✓ El correo {correo} fue eliminado")
        else:
            print(f"❌ El correo {correo} no está registrado")
            
    elif opcion == 4:
        if suscriptores:
            print("\n--- Lista de Suscriptores ---")
            for i, correo in enumerate(suscriptores, 1):
                print(f"{i}. {correo}")
            print(f"\nTotal de suscriptores: {len(suscriptores)}")
        else:
            print("\n⚠ No hay suscriptores registrados")
            
    elif opcion == 5:
        print("\n¡Hasta luego! 👋")
        break
        
    else:
        print("\n❌ Opción no válida. Por favor elige entre 1 y 5")

print("\nPrograma Terminado")
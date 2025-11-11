suscriptores = set()

while True:
    print("==========PANEL DE SUSCRIPCIONES===========")
    print("1: Agregar Nuevo correo")
    print("2: Verificar si un usario ya existe")
    print("3: Cancelar la suscripcion de un usuario")

    try: 
        opcion = int(input("¿Que opcion eliges?"))
    except ValueError:
        print("Digitaste un valor incorrecto")
        continue
    
    if opcion == 1: 
        correo = input("Digita el correo del nuevo suscriptor")

        if correo in suscriptores: 
            print("Este usuario ya existe")
        

print("Programa Terminado")
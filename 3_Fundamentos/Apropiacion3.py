correcto = True
contraseña = "1234"
conteo = 0
while correcto:
    conteo += 1
    usser = input("Ingresa la contraseña: \n")
    if contraseña == usser:
        print("La contraseña se correcta ")
        correcto = False

    else :
       if conteo < 5:
        print(f"La contraseña es incorrecta, intentalo de nuevo tienes 5 de {conteo}")
       else: 
          print(f"La contraseña es incorrecta, Numero de intentos maximos alcanzados")
          correcto = False

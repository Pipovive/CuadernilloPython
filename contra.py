valido = False
mayus = False
minus = False
number = False
simbolo = False
simbolos = "!@#$%^&*()-_=+[]{};:,.<>?/\\|`~"

while valido != True: 
    contraseña = input("Digira una contraseña que tenga: 8 digitos, 1 mayuculas, 1 minuscula, 1 numero")
    if contraseña.count() >= 8:
        number = True

    for letra in contraseña:
        
        if letra.isupper:
            mayus = True
            print("La contraseña SI tiene: mayusculas")
        if letra.islower:
            minus = True
            print("La contraseña SI tiene: minusculas")
        if letra.isdigit:
            numer = True
            print("La contraseña SI tiene: numeros")
        if letra in simbolos:
            simbolo = True
            print("La contraseña SI tiene: simbolos")

    
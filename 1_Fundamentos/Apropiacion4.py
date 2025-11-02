numero1 = int(input("Digita un numero\n"))
numero2 = int(input("Digita un numero\n"))
numero3 = int(input("Digita un numero\n"))

verficado = (
    numero1 == numero2  or 
    numero1 == numero3 or 
    numero2 == numero3
)


print("Al menos dos de los númerosson iguales:", verficado)


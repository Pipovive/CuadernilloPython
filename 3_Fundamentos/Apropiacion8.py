numero = int(input("Digita un numero para conocer su factorial: \n"))
suma = 0

for i in range(numero-1, 0, -1):
    factorial  = numero * i
    suma += factorial
    print(f"Conteo factorial {i} * {numero}:  {factorial}")

print(f"\n El total factorial es: {suma}")
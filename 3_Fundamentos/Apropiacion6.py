array = []
par = 0
impar = 0
numero_usuarios = input("Ingresa una secuencia de numeros: \n")
elemento_str = numero_usuarios.split(',')

for elemento in elemento_str:
    numero = int(elemento)
    if (numero % 2) == 0:
        par += 1
    else:
        impar += 1


print(f"El numero de pares es: \n{par}")
print(f"El numero de impares es: \n{impar}")


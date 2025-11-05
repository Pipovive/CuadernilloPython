# Pedir los dos números
num1 = int(input("Digita el primer número: "))
num2 = int(input("Digita el segundo número: "))

# Función para calcular la suma de los divisores propios
def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

# Calcular las sumas
suma1 = suma_divisores(num1)
suma2 = suma_divisores(num2)

# Verificar si son amigos
if suma1 == num2 and suma2 == num1:
    print(f"{num1} y {num2} son números amigos 😊")
else:
    print(f"{num1} y {num2} NO son números amigos 😢")


num1 = int(input("Digita un numero para saber si es amigo: \n"))
num2 = int(input("Digita un numero para saber si es amigo\n" ))

def reconocedor_amigos (n):
    suma = 0
    for i in range(1,n):
        if n % 2 == 0:
            suma += i
    return suma
    
num1 = reconocedor_amigos(num1)
num2 = reconocedor_amigos(num2)

if (num1 == num2 or num2 == num1):
    print(f"El numero {num1} y {num2} son amigos")
else :
    print(f"El numero {num1} y {num2} son amigos")
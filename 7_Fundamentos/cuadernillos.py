import random
frutas = ['manzanas', 'mango', 'papaya', 'banana', 'melon', 'uva', 'pera', 'piña']
# print(len(frutas))

numeros = [5, 6, 3, 4,7]
# print(min(numeros), max(numeros))

# print(random.sample(frutas,3))

def suma(a,b):
    return a + b

# print(suma(3,4))

def tabla_del_5 ():
    for i in range(1,11):
        print(f"{i} *  5 = {i*5}")

def tabla_del (num, limite):
    for i in range(1, limite+1):
        print(f"{num} * {i} = {num * i}")

# tabla_del(int(input("numero: ")),int(input("limite:")))


def suma(*numeros):
    print(type(numeros))

    return sum(numeros)

# print(f"La suma de los numeros es: {suma(1,3,4,5,6)}")
# print(f"La suma de los numeros es: {suma(1,3,4)}")
# print(f"La suma de los numeros es: {suma(1,3,4,5)}")

def mostrar_info(**datos):
    print(type(datos))
    for k in datos.items():
        print (k)

# mostrar_info (nombre="Julian", apellido="Valencia")

def mi_funcion():
    return 1, "a", 3.5

def procesar_numeros (numeros):
    suma = sum(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    promedio = suma / (len(numeros))

    return suma, minimo, maximo, promedio

numeros = [1,2,3,4,5]

suma, minimo, maximo, promedio = procesar_numeros(numeros)


def doblar_valor (x): 
    x = x * 2
    return x



def doblar_valores(ns):
    ns [0] = ns[0] * 2
    ns [1] = ns[1] * 2
    ns [2] = ns[2] *2
    print(f"Dentro de la función{ns}")
    
ns = [10,50,100]
doblar_valores(ns)
print(ns)
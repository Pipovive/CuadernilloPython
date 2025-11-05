cantidad = int(input("Digita la cantidad de numeros que quieres ingresar: "))
lista = []

for i in range(0,cantidad):
    n = int(input("Inserta el numero: \n"))
    lista.append(n)

lista_desordenada = sorted(lista,reverse=True)

print(f"Lista en reverso: {lista_desordenada}")
print(f"Lista en normal: {lista}")

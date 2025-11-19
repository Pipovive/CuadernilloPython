numeros=input("dime un numero :")
diccionario={
    "1": "Uno",
    "2": "Dos",
    "3": "Tres",
    "4": "Cuatro",
    "5": "Cinco",
    "6": "Seis",
    "7": "Siete",
    "8": "Ocho",
    "9": "Nueve",
}   


def convertidor_numeros(numeros):
    lista = []
    for numero in numeros:
        if numero in diccionario:
            lista.append(diccionario[numero])
    return "-".join(lista)

print(convertidor_numeros(numeros))

    
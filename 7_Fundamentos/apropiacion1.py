palabra = input("Digita una palabra")
diccionario = {}

def separador_palabras(arg):
    for letra in arg:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1

separador_palabras(palabra)

print(diccionario)
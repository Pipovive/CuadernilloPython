realizadas = ("arroz", "leche", "huevo", "pan", "queso", "cafe") 
lista_compradas = list(realizadas)

lista_compradas 

print(lista_compradas)

diccionario = {}

for llave, valor in lista_compradas:
    diccionario[llave] =  llave
    diccionario[llave][valor] = 1000 

print(diccionario)
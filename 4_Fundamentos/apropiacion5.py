import random

lista_frutas = ["manzana", "banano", "mandarina", "limon", "tomate", "kiwi"]

select = random.randint(0,len(lista_frutas))
intentos = 5

fruta_el = lista_frutas[select]

print("Bienvenido, adivina el nombre de la fruta: ")
while intentos == 0:
    intentos -= 1 
    print(f"Tienes {intentos} intentos")
    
    res = input("Escribe el nombre de la fruta:  \n").islower()
    if res != fruta_el:
        if res
    else

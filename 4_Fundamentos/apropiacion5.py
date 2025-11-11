import random

lista_frutas = ["manzana", "coco", "mango", "fresa", "banano"]

select = random.randint(0, len(lista_frutas) - 1)
intentos = 5

fruta_elegida = lista_frutas[select]
acertar = False

print("🎮 El videojuego es adivinar el nombre de la fruta:")

while intentos > 0: 
    elegido = input(f"Te quedan {intentos} intentos. Digita el nombre de la fruta: \n").lower()
    
    if elegido != fruta_elegida:
        print("❌ Incorrecto.")
        intentos -= 1
        if intentos == 4:
            print(f"Pista: la fruta tiene {len(fruta_elegida)} letras.")
        elif intentos == 3:
            print(f"Pista: empieza con '{fruta_elegida[0]}' y termina con '{fruta_elegida[-1]}'.")
    else:
        acertar = True
        break

if acertar:
    print(f"✅ ¡Felicidades! Acertaste, la fruta era: {fruta_elegida}")
else:
    print(f"😢 Te quedaste sin intentos. La fruta era: {fruta_elegida}")

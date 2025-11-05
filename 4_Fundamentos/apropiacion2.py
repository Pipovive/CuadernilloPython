frase_1 = input("Digita una frase: \n")
frase_2 = input("Digita otra frase: \n")

cadena_1 = list(frase_1)
cadena_2 = list(frase_2)

cadena_3 = []

for i in range(min(len(cadena_1),len(cadena_2))):
    if cadena_1[i] == cadena_2[i]:
        cadena_3.append(cadena_1[i])

for pos, val in enumerate(cadena_3):
    print(f"Posicion: {pos + 1} Letra: {val} ")
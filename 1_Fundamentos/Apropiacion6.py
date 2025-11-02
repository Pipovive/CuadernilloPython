cadena = input("Digita una frase:\n")
caracter = input("Ahora digita el carácter que quieres contar:\n")

cantidad = cadena.lower().count(caracter)

print(f"El carácter '{caracter}' aparece {cantidad} veces en la frase.")
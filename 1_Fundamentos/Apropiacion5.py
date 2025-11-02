cantidad_frutas_recolectadas = int(input("Digita la cantidad de frutas recolectadas"))
cantidad_frutas_producido = int(input("Digita la cantidad de frutas producido"))

indice_cosecha = (cantidad_frutas_recolectadas / cantidad_frutas_producido) * 100

print("El indice total de frutas producida es: \n" , indice_cosecha)
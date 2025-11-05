productos = []
cantidades = []
suma = 0
caja = False

while caja != True: 
    articulo = float(input("Digita el valor del articulo a comprar"))
    cantidad = int(input("Digita la cantidad del articulo a comprar"))

    productos.append(articulo)
    cantidades.append(cantidad)

    seguir = input("Vas a insertar mas prductos? (s/n)").lower()
    if seguir == "n":
        break


for i in range(len(productos)):
    valor = productos[i] * cantidades[i]
    suma += valor

if suma >= 200000:
    iva = suma * 0.19 
    descuento = suma * 0.10 

    suma = suma + descuento -  descuento

    print(f"El valor de todo es: {suma:.2f}") 

else: 
    print(f"El valor de todo es: {suma:.2f}") 
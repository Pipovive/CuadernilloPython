# Solicitar las longitudes de los lados
a = float(input("Ingrese la longitud del lado A: "))
b = float(input("Ingrese la longitud del lado B: "))
c = float(input("Ingrese la longitud del lado C: "))

# Verificar si los lados forman un triángulo válido
if a + b > c and a + c > b and b + c > a:
    # Es un triángulo válido, ahora determinar el tipo
    if a == b == c:
        print("🔺 El triángulo es EQUILÁTERO (todos los lados iguales).")
    elif a == b or a == c or b == c:
        print("🔺 El triángulo es ISÓSCELES (dos lados iguales).")
    else:
        print("🔺 El triángulo es ESCALENO (todos los lados diferentes).")
else:
    print("❌ No es un triángulo válido. La suma de dos lados debe ser mayor que el tercero.")




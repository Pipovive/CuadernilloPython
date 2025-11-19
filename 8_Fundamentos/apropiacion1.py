lista = [3, 5, 6, 8]

while True:
    try:
        pos = int(input("Ingrese la posición del elemento que desea obtener: "))
        print(f"El valor en la posición {pos} es {lista[pos]}")
        break  # Solo termina si no hay errores

    except ValueError:
        print("❌ Error: Debe ingresar un número, no una letra ni símbolo.")

    except IndexError:
        print(f"❌ Error: La posición ingresada no existe. La lista solo tiene índices del 0 al {len(lista)-1}.")

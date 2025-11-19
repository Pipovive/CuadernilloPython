def agregar_una_vez(lista, elemento):
    try:
        # Si el elemento ya está en la lista se lanza un error
        if elemento in lista:
            raise ValueError(f"Error: Imposible añadir elementos duplicados => {elemento}.")
        else:
            lista.append(elemento)
            print(f"Elemento '{elemento}' agregado correctamente.")
    except ValueError as e:
        # Captura y muestra el mensaje de error
        print(e)
    finally:
        # Se ejecuta siempre
        print("Gracias por usar este programa")


# Ejemplos de prueba:
mi_lista = [1, 2, 3]

agregar_una_vez(mi_lista, 4)   # Se agrega
agregar_una_vez(mi_lista, 2)   # Error
print(mi_lista)

numero_personas = int(input("Digita el numero de personas que van a comer pizza\n"))
eleccion = input("Digita el tamaño de la pizza que deseas comprar: \n").capitalize()
lista_compras = []

pizzas = {
    "Pequeña": 6,
    "Mediana": 8,
    "Grande": 10
}

def rebanador(eleccion, numero_personas):
    # Si no hay elección, usar Grande por defecto
    if eleccion == "" or eleccion not in pizzas:
        eleccion = "Grande"
    
    rebanadas_por_pizza = pizzas[eleccion]
    
    # Calcular cuántas pizzas completas necesitamos
    pizzas_necesarias = numero_personas // rebanadas_por_pizza
    rebanadas_faltantes = numero_personas % rebanadas_por_pizza
    
    # Agregar las pizzas completas del tamaño elegido
    for _ in range(pizzas_necesarias):
        lista_compras.append(eleccion)
    
    # Si sobran rebanadas, agregar una pizza adicional del tamaño más apropiado
    if rebanadas_faltantes > 0:
        if rebanadas_faltantes <= 6:
            lista_compras.append("Pequeña")
        elif rebanadas_faltantes <= 8:
            lista_compras.append("Mediana")
        else:
            lista_compras.append("Grande")
    
    return lista_compras

# Llamar la función
resultado = rebanador(eleccion, numero_personas)
print(f"\nNecesitas comprar: {resultado}")
print(f"Total de pizzas: {len(resultado)}")
# Solicitar datos al usuario
peso = float(input("Ingrese el peso del paquete (en kg): "))
destino = input("Ingrese el destino (nacional/internacional): ").lower()

# Inicializar variable para el costo
costo = 0

# Calcular el costo según el peso y destino
if destino == "nacional":
    if 0 <= peso <= 3:
        costo = 29340
    elif 4 <= peso <= 7:
        costo = 55470
    elif 8 <= peso <= 10:
        costo = 75450
    elif 11 <= peso <= 15:
        costo = 108540
    elif 16 <= peso <= 20:
        costo = 141540
    elif peso > 20:
        # Se cobra la tarifa base de 20 kg más el adicional
        costo = 141540 + (peso - 20) * 6840
    else:
        print("Peso inválido.")

elif destino == "internacional":
    if 0 <= peso <= 3:
        costo = 46380
    elif 4 <= peso <= 7:
        costo = 100380
    elif 8 <= peso <= 10:
        costo = 132780
    elif 11 <= peso <= 15:
        costo = 186780
    elif 16 <= peso <= 20:
        costo = 240780
    elif peso > 20:
        costo = 240780 + (peso - 20) * 12000
    else:
        print("Peso inválido.")
else:
    print("Destino inválido.")

# Mostrar el resultado
if costo > 0:
    print(f"\n--- Resultado del Envío ---")
    print(f"Destino: {destino.capitalize()}")
    print(f"Peso: {peso} kg")
    print(f"Costo total: ${costo:,.0f} COP")

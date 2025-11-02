# Leer la entrada binaria del producto
entrada = input("Entrada binaria (1 = cumple, 0 = no cumple): ")

# Verificar si hay algún estándar no cumplido
if "0" in entrada:
    print("Resultado: ❌ PIEZA RECHAZADA")
    print("Motivo: No cumplió todos los estándares de calidad.")
else:
    print("Resultado: ✅ PIEZA APROBADA")
    print("Motivo: Cumplió todos los estándares de calidad.")


# entrada = input("Entrada Binaria:")

# print("El producto esta listo: ", "ALERTA, no cumplio todos los requisitos" if entrada.count("0") else "Si, cumplio todos los requisitos" )
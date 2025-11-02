import random

tabla = int(input("¿Qué tabla quieres repasar? (del 1 al 10): "))
correctas = 0
contador = 0

while contador < 6:
    numero = random.randint(1, 10)
    respuesta = int(input(f"¿Cuánto es {tabla} x {numero}? "))

    if respuesta == tabla * numero:
        print("¡Correcto! Muy bien, sigue así 😊")
        correctas += 1
    else:
        print(f"Incorrecto. La respuesta correcta es {tabla * numero}.")
    
    contador += 1

print(f"\nRespondiste correctamente {correctas} de 6 preguntas.")

if correctas == 6:
    print("¡Excelente! Te sabes la tabla muy bien. Ahora puedes repasar otras tablas.")
elif correctas >= 3:
    print("Buen trabajo, sigue practicando esta tabla para mejorar aún más.")
else:
    print("Es recomendable que sigas estudiando esta tabla.")

# Mostrar la tabla completa
print(f"\nTabla del {tabla}:")
i = 1
while i <= 10:
    print(f"{tabla} x {i} = {tabla * i}")
    i += 1

# Preguntar si quiere repetir
opcion = input("\n¿Quieres volver a estudiarla? (sí/no): ").lower()
if opcion in ["sí", "si"]:
    print("Repite el programa para volver a estudiar la tabla.")
else:
    print("¡Hasta luego! Sigue practicando.")

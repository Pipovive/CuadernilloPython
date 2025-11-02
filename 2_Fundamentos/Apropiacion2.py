estrato = int(input("Digita tu estrato:\n"))
edad = int(input("Digita tu edad:\n"))
matricula = float(input("Digita el valor de la matrícula:\n"))

if estrato == 1 and edad < 18:
    descuento = matricula * 0.20
elif estrato == 1 and edad >= 18:
    descuento = matricula * 0.15
elif estrato == 2 and edad < 18:
    descuento = matricula * 0.10
elif estrato == 2 and edad >= 18:
    descuento = matricula * 0.05
else:
    descuento = 0

valor_final = matricula - descuento

print(f"\n--- Resultado ---")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar: ${valor_final:.2f}")

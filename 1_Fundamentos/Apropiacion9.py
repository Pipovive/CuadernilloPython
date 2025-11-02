import math


t1 = float(input("Digita el valor de tu primera transacción: "))
t2 = float(input("Digita el valor de tu segunda transacción: "))
t3 = float(input("Digita el valor de tu tercera transacción: "))
t4 = float(input("Digita el valor de tu cuarta transacción: "))
t5 = float(input("Digita el valor de tu quinta transacción: "))


r1 = math.ceil(t1)
r2 = math.ceil(t2)
r3 = math.ceil(t3)
r4 = math.ceil(t4)
r5 = math.ceil(t5)


d1 = r1 - t1
d2 = r2 - t2
d3 = r3 - t3
d4 = r4 - t4
d5 = r5 - t5


total_redondeado = r1 + r2 + r3 + r4 + r5
total_perdido = d1 + d2 + d3 + d4 + d5


print("\n--- Resultados ---")
print(f"Transacción 1: {t1:.3f} → {r1}")
print(f"Transacción 2: {t2:.3f} → {r2}")
print(f"Transacción 3: {t3:.3f} → {r3}")
print(f"Transacción 4: {t4:.3f} → {r4}")
print(f"Transacción 5: {t5:.3f} → {r5}")

print("\n--- Totales ---")
print(f"Suma redondeada: {total_redondeado}")
print(f"Total perdido por redondeo: {total_perdido:.3f}")

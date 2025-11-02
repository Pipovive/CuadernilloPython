import random

num1 = random.randint(1,10)
num2 = random.randint(1,10)

suma = num1 + num2

print(f"La suma de los numeros es: ${suma:2f}")

adivina1 = int(input("Adivina el primer número: "))
adivina2 = int(input("Adivina el segundo número: "))

if (adivina1 == num1 and adivina2 == num2) or (adivina1 == num2 and adivina2 == num1):
    print("🎉 ¡Correcto! Adivinaste los dos números.")
else:
    print(f"❌ Incorrecto. Los números eran {num1} y {num2}.")
import random

# Pedir al usuario 6 números
numeros_usuario = []
print("🎰 Bienvenido a la Lotería 🎰")
for i in range(6):
    numero = int(input(f"Ingrese el número {i+1} (entre 1 y 49): "))
    numeros_usuario.append(numero)

# Generar 6 números aleatorios del 1 al 49
numeros_ganadores = random.sample(range(1, 50), 6)

# Mostrar los números ganadores
print("\nNúmeros ganadores:", numeros_ganadores)
print("Tus números:", numeros_usuario)

# Calcular cuántos números coinciden
aciertos = len(set(numeros_usuario) & set(numeros_ganadores))

# Mostrar el número de aciertos
print(f"\n🎯 Has acertado {aciertos} número(s).")

# Determinar el premio según los aciertos
if aciertos == 6:
    print("🏆 ¡Felicidades! Has ganado el premio mayor 💰💰💰")
elif aciertos == 5:
    print("🥈 ¡Excelente! Ganaste el segundo premio 💵")
elif aciertos == 4:
    print("🥉 Muy bien, ganaste un premio pequeño 💸")
elif aciertos == 3:
    print("✨ Aciertos decentes, te llevas una recompensa simbólica 💫")
else:
    print("😢 No hubo suerte esta vez. ¡Sigue intentando!")

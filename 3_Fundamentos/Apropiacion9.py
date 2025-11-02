import time  # para pausar 1 segundo entre cada número

contador = int(input("Digita el tiempo del contador: "))

while contador >= 0:
    print(f"Su tiempo es: {contador}")
    time.sleep(1)  # espera 1 segundo antes de continuar
    contador -= 1

print("⏰ ¡Tiempo terminado!")

# contador =  int(input("Digita el tiempo del contador: \n"))

# while contador != 0:
#     print(f"Su tiempo es:  {contador}")
#     contador -= 1
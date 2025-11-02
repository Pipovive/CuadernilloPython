temperatura = float(input("Ingrese la temperatura actual: \n"))
motor = True  

if temperatura > 80:
    motor = False 


print("Estado del motor:", "Encendido" if motor else "Apagado")

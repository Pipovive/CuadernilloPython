billetes = [50000, 20000,10000,5000,2000]
monto = int(input("Digita el dinero"))
desgloce = {}
residuo = monto

for billete in billetes:
    cantidad = residuo // billete
    residuo = residuo % billete
    desgloce[billete] = cantidad

print("--Desgloce--")

for valor, cantidad in desgloce.items():
    print(f"Billete: ({valor:.2f}) cantidad = {cantidad} ")

if residuo > 0: 
    print(f"El residuo que no puede ser expresado en billetes es: {residuo}")
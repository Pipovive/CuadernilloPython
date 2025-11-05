bandera = True
nombres = []
edades = []
sexos = []


while bandera:
    nombre = input("Digita tu nombre: \n")
    edad = int(input("Digita tu edad: \n"))
    sexo = input("Digita F o M: \n")

    nombres.append(nombre)
    edades.append(edad)
    sexos.append(sexo)

    respuesta = input("Sigue otro usuario?\n")
    
    if respuesta == "n":
        break

persona_min = edades[0]
persona_max = edades[0]
nombre_min = nombres[0]
nombre_max = nombres[0]

femenino = 0
masculino = 0

for i in range(len(edades)):
    if persona_max < edades[i]:
        persona_max = edades[i]
        nombre_max[i]
    
    if persona_min > edades[i]:
        persona_min = edades[i]
        nombre_min[i]
    
    if sexos[i] == "F":
        femenino += 1
    else: 
        masculino += 1

print("------Resultado-----")
print(f"Total masculino: {masculino}")
print(f"Total femenino: {femenino}")

print(f"La persona con mayor edad registrada fue: {nombre_max} con: {persona_max}")
print(f"La persona con menor edad registrada fue: {nombre_min} con: {persona_min}")
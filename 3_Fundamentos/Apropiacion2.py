array_boletas = []
bandera = 1
n = 0
respuesta = 1
while bandera:
   if bandera == 1:
      n += 1
      edad = int(input("Ingresa tu edad: \n"))
      estrato = int(input("Ingresa tu estrato: \n"))
      valor_boleta = float(input("Ingresa el valor de la boleta: \n"))
      
      if edad < 18 and estrato == 1:
         descuento = valor_boleta* 0.20
      elif edad >= 18 and estrato == 1: 
         descuento = valor_boleta* 0.15
      elif  edad < 18 and estrato == 2:
         descuento = valor_boleta* 0.1
      elif  edad >= 18 and estrato == 2:
         descuento = valor_boleta* 0.05
      else: 
        descuento = 0
    
      valor_boleta = valor_boleta - descuento
      print(f"El usuario: {n} \nDebe pagar: {valor_boleta}")
      array_boletas.append(valor_boleta)


      bandera = int(input("¿Alguien mas va ingresar al partido (0 = No, 1 = Si)?"))

for i, valor in enumerate(array_boletas, start=1):
    print(f"Usuario {i}: ${valor:.2f}")

print("\n¡Disfruten el partido! ⚽🎉")
       

    

   
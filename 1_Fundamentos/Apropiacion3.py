numero1 = int(input("Digita el primer número:\n"))
numero2 = int(input("Digita el segundo número:\n"))
numero3 = int(input("Digita el tercer número:\n"))

suma = numero1 + numero2 + numero3
resta = (numero1 + numero2) - numero3 
multi = numero1 * numero2 * numero3
div =   numero1  / (numero3 + numero2) 

print(f"Suma de los tres números: {suma}")
print(f"Resta del tercer número al resultado de la suma de los dos primeros: {resta}")
print(f"Multiplicación de los tres números: {multi}")
print(f"División del primer número entre la suma del segundo y el tercero: {div}")
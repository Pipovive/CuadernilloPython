# Solicitar datos al usuario
precio = float(input("Ingrese el precio del producto: $"))
cantidad = int(input("Ingrese la cantidad comprada: "))

# Calcular el total sin descuento
total = precio * cantidad

# Aplicar descuento si corresponde
if cantidad >= 10:
    descuento = total * 0.10
    total -= descuento
    print(f"\nSe aplicó un descuento del 10% (${descuento:.2f})")
else:
    print("\nNo se aplicó descuento.")

# Mostrar el total a pagar
print(f"Total a pagar: ${total:.2f}")

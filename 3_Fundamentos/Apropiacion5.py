fibonacci = [0,1]

for i in range(2, 21):
    agregar = fibonacci[i - 2] + fibonacci[i - 1]
    fibonacci.append(agregar)
    
for i in range(0,21):
    print(f"Iteracion: {i}: {fibonacci[i]}")
lista = []
salir = False

try:
    while not salir:
        print("\n📋 Listado de opciones:")
        print("1: Ingresar nueva lista")
        print("2: Ordenar lista")
        print("3: Promediar")
        print("4: Buscar número")
        print("5: Salir")

        eleccion = int(input("Digita el número de la opción: "))

        if eleccion == 1:
            print("\n🟢 Ingresar números (usa un número negativo para salir):")
            lista.clear()  # Limpia la lista anterior
            while True:
                n = int(input("Digita un número: "))
                if n >= 0:
                    lista.append(n)
                else:
                    break

        elif eleccion == 2:
            if len(lista) > 0:
                lista.sort()
                print("✅ Lista ordenada:", lista)
            else:
                print("⚠️ La lista está vacía.")

        elif eleccion == 3:
            if len(lista) > 0:
                suma = sum(lista)
                promedio = suma / len(lista)
                print(f"📊 El promedio es: {promedio:.2f}")
            else:
                print("⚠️ No hay números para promediar.")

        elif eleccion == 4:
            if len(lista) > 0:
                buscar = int(input("🔎 Digita el número que quieras buscar: "))
                if buscar in lista:
                    print("✅ El número está en la lista.")
                else:
                    print("❌ El número no está en la lista.")
            else:
                print("⚠️ La lista está vacía.")

        elif eleccion == 5:
            salir = True
            print("👋 Saliendo del programa...")

        else:
            print("❌ Opción inválida, intenta de nuevo.")

except Exception as e:
    print("❗ Ha ocurrido un error:", e)

print("✅ El programa ha terminado.")

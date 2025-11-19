import random

def tirar_dados():
    """Simula el lanzamiento de dos dados"""
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def juego_dados():
    """Función principal del juego de dados"""
    print("=" * 50)
    print("    BIENVENIDO AL JUEGO DE DADOS")
    print("=" * 50)
    
    # Solicitar número de jugadores
    while True:
        try:
            num_jugadores = int(input("\n¿Cuántas personas van a jugar? "))
            if num_jugadores > 0:
                break
            else:
                print("Debe haber al menos 1 jugador.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    # Diccionario para guardar resultados
    resultados = {}
    
    print("\n" + "=" * 50)
    print("         ¡COMIENZA EL JUEGO!")
    print("=" * 50)
    
    # Turno de cada jugador
    for turno in range(1, num_jugadores + 1):
        print(f"\n--- Turno {turno} ---")
        nombre = input("Ingresa tu nombre: ").strip()
        
        # Validar que el nombre no esté vacío
        while not nombre:
            nombre = input("El nombre no puede estar vacío. Ingresa tu nombre: ").strip()
        
        input(f"\n{nombre}, presiona Enter para lanzar los dados...")
        
        # Lanzar los dados
        dado1, dado2 = tirar_dados()
        suma = dado1 + dado2
        
        # Mostrar resultados
        print(f"🎲 Dado 1: {dado1}")
        print(f"🎲 Dado 2: {dado2}")
        print(f"✨ Suma total: {suma}")
        
        # Guardar resultado
        resultados[nombre] = suma
    
    # Mostrar resultados finales
    print("\n" + "=" * 50)
    print("         RESULTADOS FINALES")
    print("=" * 50)
    
    for nombre, puntos in resultados.items():
        print(f"{nombre}: {puntos} puntos")
    
    # Determinar el ganador
    ganador = max(resultados, key=resultados.get)
    puntos_ganador = resultados[ganador]
    
    # Verificar si hay empate
    ganadores = [nombre for nombre, puntos in resultados.items() if puntos == puntos_ganador]
    
    print("\n" + "=" * 50)
    if len(ganadores) > 1:
        print(f"🎉 ¡EMPATE! Los ganadores son:")
        for nombre in ganadores:
            print(f"   🏆 {nombre} con {puntos_ganador} puntos")
    else:
        print(f"🎉 ¡EL GANADOR ES: {ganador}!")
        print(f"   🏆 Con {puntos_ganador} puntos")
    print("=" * 50)

# Ejecutar el juego
if __name__ == "__main__":
    juego_dados()
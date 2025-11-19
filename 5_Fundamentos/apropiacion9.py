# Diccionario con juegos y sus puntajes
puntajes_juegos = {
    "Fortnite": [850, 920, 780, 1050, 900, 870],
    "Minecraft": [1200, 1350, 980, 1400, 1100],
    "Call of Duty": [2500, 2800, 2200, 3000, 2650, 2900]
}

# ===== FUNCIONES =====

def mostrar_todos_puntajes():
    """Muestra todos los juegos con sus puntajes"""
    print("\n" + "=" * 60)
    print("🎮 PUNTAJES POR JUEGO")
    print("=" * 60)
    
    for juego, puntajes in puntajes_juegos.items():
        print(f"\n{juego}:")
        print(f"  Puntajes: {puntajes}")
        print(f"  Cantidad de partidas: {len(puntajes)}")

def calcular_promedio(juego):
    """Calcula el promedio de puntajes de un juego"""
    if juego not in puntajes_juegos:
        return None
    
    puntajes = puntajes_juegos[juego]
    if len(puntajes) == 0:
        return 0
    
    promedio = sum(puntajes) / len(puntajes)
    return promedio

def mostrar_promedios():
    """Muestra los promedios de todos los juegos"""
    print("\n" + "=" * 60)
    print("📊 PROMEDIO DE PUNTAJES POR JUEGO")
    print("=" * 60)
    
    for juego in puntajes_juegos.keys():
        promedio = calcular_promedio(juego)
        print(f"\n{juego}:")
        print(f"  Promedio: {promedio:.2f} puntos")

def puntaje_maximo_minimo(juego):
    """Encuentra el puntaje máximo y mínimo de un juego"""
    if juego not in puntajes_juegos or len(puntajes_juegos[juego]) == 0:
        return None, None
    
    puntajes = puntajes_juegos[juego]
    maximo = max(puntajes)
    minimo = min(puntajes)
    
    return maximo, minimo

def agregar_puntaje():
    """Agrega un nuevo puntaje a un juego"""
    print("\n--- AGREGAR NUEVO PUNTAJE ---")
    juego = input("Nombre del juego: ").strip()
    
    if not juego:
        print("❌ El nombre no puede estar vacío")
        return
    
    try:
        puntaje = int(input("Puntaje obtenido: "))
        
        if puntaje < 0:
            print("❌ El puntaje no puede ser negativo")
            return
        
        if juego in puntajes_juegos:
            puntajes_juegos[juego].append(puntaje)
            print(f"✓ Puntaje {puntaje} agregado a {juego}")
        else:
            puntajes_juegos[juego] = [puntaje]
            print(f"✓ Nuevo juego '{juego}' creado con puntaje {puntaje}")
    except ValueError:
        print("❌ El puntaje debe ser un número")

def agregar_juego():
    """Agrega un nuevo juego con múltiples puntajes"""
    print("\n--- AGREGAR NUEVO JUEGO ---")
    juego = input("Nombre del juego: ").strip()
    
    if not juego:
        print("❌ El nombre no puede estar vacío")
        return
    
    if juego in puntajes_juegos:
        print(f"❌ El juego '{juego}' ya existe")
        return
    
    print("\nIngresa los puntajes separados por comas (ej: 100,200,300)")
    puntajes_str = input("Puntajes: ")
    
    try:
        puntajes = [int(p.strip()) for p in puntajes_str.split(",")]
        puntajes_juegos[juego] = puntajes
        print(f"✓ Juego '{juego}' agregado con {len(puntajes)} puntajes")
    except ValueError:
        print("❌ Formato incorrecto. Usa números separados por comas")

def buscar_juego():
    """Busca un juego y muestra su información completa"""
    print("\n--- BUSCAR JUEGO ---")
    juego = input("Nombre del juego a buscar: ").strip()
    
    if juego not in puntajes_juegos:
        print(f"❌ El juego '{juego}' no existe")
        return
    
    puntajes = puntajes_juegos[juego]
    promedio = calcular_promedio(juego)
    maximo, minimo = puntaje_maximo_minimo(juego)
    
    print("\n" + "=" * 60)
    print(f"🎮 INFORMACIÓN DE: {juego}")
    print("=" * 60)
    print(f"Puntajes: {puntajes}")
    print(f"Cantidad de partidas: {len(puntajes)}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Puntaje máximo: {maximo}")
    print(f"Puntaje mínimo: {minimo}")
    print("=" * 60)

def eliminar_juego():
    """Elimina un juego del diccionario"""
    print("\n--- ELIMINAR JUEGO ---")
    juego = input("Nombre del juego a eliminar: ").strip()
    
    if juego in puntajes_juegos:
        del puntajes_juegos[juego]
        print(f"✓ Juego '{juego}' eliminado")
    else:
        print(f"❌ El juego '{juego}' no existe")

def juego_mejor_promedio():
    """Encuentra el juego con mejor promedio"""
    if not puntajes_juegos:
        print("❌ No hay juegos registrados")
        return
    
    mejor_juego = None
    mejor_promedio = 0
    
    for juego in puntajes_juegos.keys():
        promedio = calcular_promedio(juego)
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_juego = juego
    
    print("\n" + "=" * 60)
    print(f"🏆 JUEGO CON MEJOR PROMEDIO: {mejor_juego}")
    print(f"    Promedio: {mejor_promedio:.2f} puntos")
    print("=" * 60)

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 60)
    print("           🎮 SISTEMA DE PUNTAJES DE JUEGOS 🎮")
    print("=" * 60)
    print("1.  Ver todos los puntajes")
    print("2.  Ver promedios de todos los juegos")
    print("3.  Buscar juego específico")
    print("4.  Agregar puntaje a un juego existente")
    print("5.  Agregar nuevo juego")
    print("6.  Eliminar juego")
    print("7.  Ver juego con mejor promedio")
    print("8.  Salir")
    print("=" * 60)

# ===== PROGRAMA PRINCIPAL =====

def main():
    print("\n¡Bienvenido al Sistema de Puntajes de Juegos!")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\nSelecciona una opción (1-8): "))
        except ValueError:
            print("\n❌ Por favor ingresa un número válido")
            continue
        
        if opcion == 1:
            mostrar_todos_puntajes()
            
        elif opcion == 2:
            mostrar_promedios()
            
        elif opcion == 3:
            buscar_juego()
            
        elif opcion == 4:
            agregar_puntaje()
            
        elif opcion == 5:
            agregar_juego()
            
        elif opcion == 6:
            eliminar_juego()
            
        elif opcion == 7:
            juego_mejor_promedio()
            
        elif opcion == 8:
            print("\n¡Gracias por usar el sistema! 🎮👋")
            break
            
        else:
            print("\n❌ Opción no válida. Elige entre 1 y 8")

# Ejecutar el programa
if __name__ == "__main__":
    main()
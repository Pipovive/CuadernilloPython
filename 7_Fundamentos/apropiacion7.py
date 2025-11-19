import random

def intentar_examen(puntaje, intentos=1, puntaje_minimo=70):
    """
    Función recursiva que cuenta los intentos de un aspirante para aprobar el examen del SENA.
    
    Parámetros:
    - puntaje: Puntaje obtenido en el intento actual (0-100)
    - intentos: Número de intentos realizados (por defecto 1)
    - puntaje_minimo: Puntaje necesario para aprobar (por defecto 70)
    
    Retorna:
    - Número total de intentos realizados
    """
    
    print(f"Intento #{intentos}: Puntaje obtenido = {puntaje} puntos")
    
    # Caso base: El aspirante aprobó
    if puntaje >= puntaje_minimo:
        print(f"✅ ¡FELICIDADES! Aprobaste el examen en el intento #{intentos}")
        print(f"🎯 Puntaje final: {puntaje} puntos")
        return intentos
    
    # Caso recursivo: No aprobó, debe intentar de nuevo
    else:
        print(f"❌ No aprobaste. Necesitas mínimo {puntaje_minimo} puntos.")
        print(f"   Te faltan {puntaje_minimo - puntaje} puntos. ¡Sigue intentando!\n")
        
        # Generar nuevo puntaje aleatorio para el siguiente intento
        nuevo_puntaje = random.randint(0, 100)
        
        # Llamada recursiva con el nuevo puntaje e incrementando los intentos
        return intentar_examen(nuevo_puntaje, intentos + 1, puntaje_minimo)


def simulacion_completa():
    """Función principal para ejecutar la simulación"""
    print("=" * 60)
    print("    SIMULACIÓN DE EXAMEN DE INGRESO AL SENA")
    print("=" * 60)
    print(f"📋 Puntaje mínimo para aprobar: 70 puntos")
    print(f"📊 Rango de puntajes: 0 - 100 puntos")
    print("=" * 60)
    print()
    
    # Generar puntaje aleatorio para el primer intento
    puntaje_inicial = random.randint(0, 100)
    
    # Llamar a la función recursiva
    total_intentos = intentar_examen(puntaje_inicial)
    
    print("\n" + "=" * 60)
    print(f"📈 RESUMEN: Total de intentos realizados = {total_intentos}")
    print("=" * 60)


# Versión alternativa: Función recursiva más simple (solo con puntaje como parámetro)
def intentar_examen_simple(puntaje, intentos=1):
    """Versión simplificada de la función recursiva"""
    PUNTAJE_MINIMO = 70  # Definido en el código como constante
    
    print(f"Intento {intentos}: {puntaje} puntos", end=" ")
    
    if puntaje >= PUNTAJE_MINIMO:
        print("✅ ¡Aprobado!")
        return intentos
    else:
        print("❌ Reprobado")
        return intentar_examen_simple(random.randint(0, 100), intentos + 1)


# Ejecutar la simulación
if __name__ == "__main__":
    print("\n🎓 VERSIÓN DETALLADA:")
    print("-" * 60)
    simulacion_completa()
    
    print("\n\n🎓 VERSIÓN SIMPLE:")
    print("-" * 60)
    puntaje_inicio = random.randint(0, 100)
    total = intentar_examen_simple(puntaje_inicio)
    print(f"\nTotal de intentos: {total}")
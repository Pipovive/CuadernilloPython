calificacion1 = float(input("Digita tu primera calificación: "))
calificacion2 = float(input("Digita tu segunda calificación: "))
calificacion3 = float(input("Digita tu tercera calificación: "))
examen_final = float(input("Digita la calificación de tu examen final: "))
trabajo_final = float(input("Digita la calificación de tu trabajo final: "))


promedio_parciales = (calificacion1 + calificacion2 + calificacion3) / 3


resultado = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)


print("\n--- Resultados ---")
print(f"Primer calificación: {calificacion1}")
print(f"Segunda calificación: {calificacion2}")
print(f"Tercera calificación: {calificacion3}")
print(f"Promedio de parciales: {promedio_parciales:.2f}")
print(f"Examen final: {examen_final}")
print(f"Trabajo final: {trabajo_final}")
print(f"\nCalificación final: {resultado:.2f}")
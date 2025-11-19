import pandas as pd
import seaborn as sns
import matplotlib.pyplot as ptl

# Leer archivo
df = pd.read_csv('datos.csv', index_col=0)

# Agrupar por nombre y obtener promedio de edad
edad_nombres = df.groupby('nombre')['edad'].mean().reset_index()

# Estilos
sns.set_theme(context='paper', style='dark', font='sans-serif')

# Tamaño de gráfica
ptl.figure(figsize=(10,6))

# Gráfico
sns.barplot(data=edad_nombres, x='nombre', y='edad')

# Etiquetas
ptl.xlabel("Nombres")
ptl.ylabel("Edad")
ptl.title("Promedio de Edad por Persona")
ptl.xticks(rotation=45)

# Filtrar personas cuyo promedio de edad sea mayor de 30
promedio_mayores_30 = df.groupby('nombre').filter(lambda x: x['edad'].mean() > 30)

print("\nPersonas con promedio de edad mayor a 30:\n")
print(promedio_mayores_30)

# Mostrar gráfico
ptl.show()

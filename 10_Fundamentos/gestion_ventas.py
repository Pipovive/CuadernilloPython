import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ventas.csv', index_col=0)
ventas_por_producto = df.groupby('nombre_producto')['cantidad_vendida'].sum().reset_index()

header = df.head(10)


sns.set_theme(style="whitegrid", palette="viridis", font_scale=1.1)

plt.figure(figsize=(10,6))
sns.barplot(data=ventas_por_producto, x='nombre_producto', y='cantidad_vendida')

plt.title("Ventas totales por producto", fontsize=15, fontweight="bold")
plt.xlabel("Producto")
plt.ylabel("Cantidad Vendida")
plt.xticks(rotation=45)

plt.show()
print(ventas_por_producto)
print(header)
import pandas as pd
import matplotlib.pyplot as plt

calidad__aire = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)

calidad__aire.plot()
plt.show()
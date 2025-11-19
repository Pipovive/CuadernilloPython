import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic.csv",index_col=0, parse_dates=True)

titanic.plot()
plt.show()

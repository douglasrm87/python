# https://indianaiproduction.com/matplotlib-pie-chart/
import pandas as pd
from IPython.display import Image, display
# importing matplotlib library
import matplotlib.pyplot as plt

colors = ["pink", 'blue','red','yellow','green']
# creating dataframe
df = pd.DataFrame({
	'Objetos': ['Mesa', 'Cadeira', 'Mouse', 'Teclado', 'Notebook'],
	'Price': [45.90, 38, 90, 60, 40]
})

# plotting a pie chart
plt.pie(df["Price"], labels=df["Objetos"] , colors =colors, autopct = "%0.2f%%")
# Saving the plot to a file since plt.show() may not work in VSCode web
plt.savefig('/workspaces/python/bigdata/sparkgraficos/graficoPizza.png')


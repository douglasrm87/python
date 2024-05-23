# https://indianaiproduction.com/matplotlib-pie-chart/
import pandas as pd
# importing matplotlib library
import matplotlib.pyplot as plt

colors = ["c", 'b','r','y','g']
# creating dataframe
df = pd.DataFrame({
	'Object': ['Mesa', 'Cadeira', 'Mouse', 'Teclado', 'Notebook'],
	'Price': [45.90, 38, 90, 60, 40]
})

# plotting a pie chart
plt.pie(df["Price"], labels=df["Object"] , colors =colors, autopct = "%0.2f%%")
plt.xlabel('Eixo Y')
plt.ylabel('Eixo X')
plt.show()
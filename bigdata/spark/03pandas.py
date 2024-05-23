#https://www.geeksforgeeks.org/how-to-combine-groupby-and-multiple-aggregate-functions-in-pandas/?ref=lbp
# import library
import pandas as pd
  
# import csv file
df = pd.read_csv("https://bit.ly/drinksbycountry")
# print (df.head())

# Find the average of each continent
# by grouping the data
# based on the "continent".
gContinente = df.groupby(["continent"]).mean()
# print (gContinente)

# here sum, minimum and maximum of column
# beer_servings is calculatad
agregar = df.beer_servings.agg(["sum", "min", "max"])
print (agregar)

# find an aggregation of column "beer_servings"
# by grouping the "continent" column.
agrgContinente = df.groupby(df["continent"]).beer_servings.agg(["min","max",	"sum","count","mean"])
print (agrgContinente)


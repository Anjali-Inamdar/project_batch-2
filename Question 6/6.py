import pandas as pd
# import plotly.express as px
# import numpy as np

usa_sales = pd.read_csv("data/us_sales_2000_to_2016.csv")
products = pd.read_csv("data/product_master.csv")
usa_master = pd.read_csv("data/zip_usa_master.csv")

usa_master.rename(columns={"PostalCode" : "Zip"}, inplace=True) #rename PostalCode of zip_usa_master csv file to Zip bcz we need to merge the columns
new_famous = pd.merge(usa_master, usa_sales, on="Zip")
# print(new_famous)
result = new_famous[new_famous["PlaceName"] == "Fort Worth"]
# print(result)
x = result.groupby("ProductID")["Units"].sum().idxmax() #takes the Index of product of having highest unit sold
#print(products[products["ProductID"] == x])
print("The most famous product in Fort Worth Texas is", products[products["ProductID"] == x]["Product"].values)

import pandas as pd
import numpy as np

usa_sales = pd.read_csv("data/us_sales_2000_to_2016.csv")
products = pd.read_csv("data/product_master.csv")

new = pd.merge(products, usa_sales, on="ProductID")
new["year"] = pd.DatetimeIndex(new["Date"]).year

result = new.groupby(["year", "ProductID"])["Units"].sum()
top_product_ids = result.groupby('year', group_keys=False).apply(lambda x: x.nlargest(5)).reset_index()
ids = top_product_ids["ProductID"].tolist()

ids = np.reshape(ids, (17, 5)) #17, 5
print(ids)

for i in range(len(ids)):
    print("For year " , 2000+i , " ")
    for j in range(5):
        print(j+1, " ", products[products["ProductID"] == ids[i][j]]["Product"].values)
    print()
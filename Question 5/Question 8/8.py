import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

usa_sales = pd.read_csv("data/us_sales_2000_to_2016.csv")
products = pd.read_csv("data/product_master.csv")
usa_master = pd.read_csv("data/zip_usa_master.csv")


usa_master.rename(columns={"PostalCode" : "Zip"}, inplace=True)
least_revenue_location = pd.merge(usa_master, usa_sales, on="Zip")
sample_data = pd.read_csv("data/sample_data.csv")

#Company Should work on their quarter 1 and 4 to generate more revenue.
quarter_revenue = sb.barplot(x = sample_data["year"], y = sample_data["Quarterly Revenue"] / 1000000, hue=sample_data["month"])
quarter_revenue.set_ylabel("Quarter Revenue in millions USD")
quarter_revenue.set_xlabel("Years")
plt.legend(title="Quarters")
plt.xticks(rotation=45) #rotate in y axis by 45 degree
plt.show()

#Comapny Should increase the number of items sold in these areas.

print("Comapny Should increase the number of items sold in these areas. Because company is unable to generate revenue from these areas.\n")
least_revenue_location["year"] = pd.DatetimeIndex(least_revenue_location["Date"]).year
least_revenue_location = least_revenue_location[(least_revenue_location["year"] == 2015) | (least_revenue_location["year"] == 2016)]
result = least_revenue_location.groupby(["year", "PlaceName"])["Units"].sum()
res = result.groupby('year', group_keys=False).apply(lambda x: x.nsmallest(10)).reset_index()
print(res)
print()

#Company should increase the units sold of these items.
print("Company should increase the units sold of these items. Because these items have least sold units.\n")
new = pd.merge(products, usa_sales, on="ProductID")
new["year"] = pd.DatetimeIndex(new["Date"]).year
result = new.groupby(["year", "ProductID"])["Units"].sum()
bottom_product_ids = result.groupby('year', group_keys=False).apply(lambda x: x.nsmallest(5)).reset_index()
ids = bottom_product_ids["ProductID"].tolist()
ids = np.reshape(ids, (17, 5))
ids = ids[15:17]

for i in range(len(ids)):
    for j in range(5):
        print("For year " , 2015+i , " " , products[products["ProductID"] == ids[i][j]]["Product"].values)

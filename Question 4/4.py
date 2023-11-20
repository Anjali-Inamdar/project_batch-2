import pandas as pd
import plotly.express as px

usa_sales = pd.read_csv("data/us_sales_2000_to_2016.csv")
products = pd.read_csv("data/product_master.csv")

new = pd.merge(products, usa_sales, on="ProductID")# merging 2 csv files with productID
new["year"] = pd.DatetimeIndex(new["Date"]).year #paticular year from date

result = new.groupby(['year', "Product"])['Revenue'].sum() 
res = result.groupby('year', group_keys=False).apply(lambda x : x.nlargest(1)).reset_index() #highest of all
print(res)


fig = px.bar(res, x='year', y='Revenue', title="vtgf").update_layout(xaxis_title="Year", yaxis_title="Revenue")
fig.show()
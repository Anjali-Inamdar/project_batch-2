import pandas as pd
import plotly.express as px

file=pd.read_csv("data/us_sales_2000_to_2016.csv")

df=pd.DataFrame()
df["Year"]=pd.to_datetime(file["Date"]).dt.year
df["Quater"]=pd.to_datetime(file["Date"]).dt.quarter
df["Revenue"]=file["Revenue"].copy()

Quarterly_Sales=df.groupby(["Year",'Quater'])['Revenue'].sum()
print(Quarterly_Sales)

# disp = px.bar(Quarterly_Sales , x='Year', y='Quater')
# disp.show()
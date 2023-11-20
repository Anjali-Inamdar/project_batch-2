import pandas as pd
import plotly.express as px
sales_data=pd.read_csv('data/us_sales_2000_to_2016.csv')
sales_data['Date']=pd.to_datetime(sales_data['Date'])
sales_data.info()
sales_data["Year"]=sales_data['Date'].dt.year
print(sales_data)

y_units=sales_data.groupby("Year")["Units"].sum().reset_index()
print(y_units)
disp = px.bar(y_units , x='Year', y='Units')
disp.show()

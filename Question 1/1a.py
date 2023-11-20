import pandas as pd
import plotly.express as px
sales_file = pd.read_csv('data/us_sales_2000_to_2016.csv')
file_copy = sales_file.copy(deep=True)

# print(file)
file=pd.DataFrame()
file["Date"] = pd.to_datetime(sales_file["Date"])

file["Year"] = sales_file["Date"].dt.year
# print(file)
yearly_sales = sales_file.groupby("Year")["Revenue"].sum().reset_index()
print(yearly_sales)
fig = px.bar(yearly_sales, x='Year', y='Revenue', title="Yearly Sales of the Client").update_layout(
    xaxis_title="Year", yaxis_title="Revenue in (USD)"
)
fig.show()
import pandas as pd
file=pd.read_csv("data/us_sales_2000_to_2016.csv")

df=pd.DataFrame()
df["Year"]=pd.to_datetime(file["Date"]).dt.year
df["Revenue"]=file["Revenue"]

revenue_max=file["Revenue"].max()

ques_Q1=df.groupby("Year",as_index=True)['Revenue'].mean()
total=revenue_max-ques_Q1
print(total)


# print(revenue_max)
import pandas as pd

file=pd.read_csv("data/us_sales_2000_to_2016.csv")

df=pd.DataFrame()
df["Year_Q1"]=pd.to_datetime(file["Date"]).dt.year
df["Quater"]=pd.to_datetime(file["Date"]).dt.quarter
df["Units"]=file["Units"].copy()
# df["Revenue_Q1"]=file["Revenue"].copy()

ques_Q1=df.groupby(["Year_Q1",'Quater'])['Units'].sum()
print(ques_Q1)
import pandas as pd 
us_sales_data = pd.read_csv('data/us_sales_2000_to_2016.csv')
highest_revenue = us_sales_data["Revenue"].max()
print(highest_revenue)
lowest_revenue = us_sales_data['Revenue'].min()
print(lowest_revenue)
diff_high_low = highest_revenue - lowest_revenue
print(diff_high_low)
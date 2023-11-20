import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

sample_data = pd.read_csv("data/sample_data.csv")

sold_units = sample_data.groupby("month")["Units Sold"].sum()
print(sold_units)

sold_revenue = sample_data.groupby("month")["Quarterly Revenue"].sum()
print(sold_revenue)
quarter_revenue = sb.barplot(x = sample_data["year"], y = sample_data["Quarterly Revenue"]/1000000, hue=sample_data["month"])
quarter_revenue.set_ylabel("Quarter Revenue in (millions USD)")
quarter_revenue.set_xlabel("Years")
print(quarter_revenue)
plt.legend(title = "Quarter")
# plt.xticks(rotation=45) #rotate in y axis by 45 degree
plt.show()

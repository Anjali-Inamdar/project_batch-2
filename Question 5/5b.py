import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

sample_data = pd.read_csv("data/sample_data.csv")

sold_units = sample_data.groupby("month")["Units Sold"].sum()
print(sold_units)

quarter_units = sb.barplot(x = sample_data["year"], y = sample_data["Quarterly Unit Sold"], hue = sample_data["month"])
quarter_units.set_ylabel("Quarterly Units Sold")
quarter_units.set_xlabel("Years")
plt.legend(title = "Quarter")
plt.xticks(rotation=45) #rotate in y axis by 45 degree
plt.show()
import pandas as pd
import time

df = pd.read_csv("sales_data.csv")

start_time = time.perf_counter()

totals = []

for i in range(len(df)):
    total = df.loc[i, "Quantity"] * df.loc[i, "Price"]
    totals.append(total)

df["Total_Sales"] = totals

end_time = time.perf_counter()

print("Slow transformation completed.")
print("Rows processed:", len(df))
print("Time taken:", end_time - start_time, "seconds")
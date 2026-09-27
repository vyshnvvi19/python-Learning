import pandas as pd
import time

df = pd.read_csv("sales_data.csv")

start_time = time.perf_counter()

df["Total_Sales"] = df["Quantity"] * df["Price"]

end_time = time.perf_counter()

print("Vectorized transformation completed.")
print("Rows processed:", len(df))
print("Time taken:", end_time - start_time, "seconds")
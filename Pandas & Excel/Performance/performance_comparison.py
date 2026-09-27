import pandas as pd
import time

df = pd.read_csv("sales_data.csv")

# Slow transformation
slow_df = df.copy()

start_time = time.perf_counter()

totals = []

for i in range(len(slow_df)):
    total = slow_df.loc[i, "Quantity"] * slow_df.loc[i, "Price"]
    totals.append(total)

slow_df["Total_Sales"] = totals

slow_time = time.perf_counter() - start_time


# Vectorized transformation
vectorized_df = df.copy()

start_time = time.perf_counter()

vectorized_df["Total_Sales"] = (
    vectorized_df["Quantity"] * vectorized_df["Price"]
)

vectorized_time = time.perf_counter() - start_time


# Results
print("PERFORMANCE COMPARISON")
print("======================")
print("Rows processed:", len(df))

print("\nSlow transformation:")
print("Time:", slow_time, "seconds")

print("\nVectorized transformation:")
print("Time:", vectorized_time, "seconds")

if vectorized_time < slow_time:
    print("\nVectorized transformation was faster.")
else:
    print("\nSlow transformation was faster in this run.")
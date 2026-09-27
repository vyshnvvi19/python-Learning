import pandas as pd


print("MEMORY AWARENESS")
print("================")

df = pd.read_csv("sales_data.csv")

print("Rows:", len(df))
print("Columns:", len(df.columns))

memory_used = df.memory_usage(deep=True).sum()

print("Memory used:", memory_used, "bytes")
print("Memory used:", round(memory_used / (1024 * 1024), 2), "MB")


print("\nCHUNKING")
print("========")

total_rows = 0

for chunk in pd.read_csv("sales_data.csv", chunksize=10000):
    total_rows += len(chunk)
    print("Processed chunk:", len(chunk), "rows")

print("\nTotal rows processed using chunks:", total_rows)
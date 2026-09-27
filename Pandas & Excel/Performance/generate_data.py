import pandas as pd
import random

rows = 100000

data = {
    "Quantity": [random.randint(1, 20) for _ in range(rows)],
    "Price": [random.randint(100, 50000) for _ in range(rows)]
}

df = pd.DataFrame(data)

df.to_csv("sales_data.csv", index=False)

print("Large dataset created successfully.")
print("Rows:", len(df))
import pandas as pd

df = pd.read_csv("python-basics/day4_pandas/data.csv")

# Add new columns
df["is_adult"] = df["age"] >=18
df["high_income"] = df["salary"] > 30000

# Save output
df.to_csv("python-basics/day4_pandas/output.csv", index=False)

print(df)
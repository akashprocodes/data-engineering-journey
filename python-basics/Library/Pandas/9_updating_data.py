import pandas as pd

df = pd.read_csv("Library/Pandas/employe.csv")
print(df)

# Update value in dataset
df.loc[0,"Salary"] = 120000
print(df)
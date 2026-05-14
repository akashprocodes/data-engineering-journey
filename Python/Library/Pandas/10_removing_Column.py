import pandas as pd

df = pd.read_csv("Library/Pandas/employe.csv")
print("\nThis is normal data\n")
print(df)

#Update data here
print("\nThis is updated data\n")
df.drop(columns=["Performance-Score"], inplace=True)
print(df)
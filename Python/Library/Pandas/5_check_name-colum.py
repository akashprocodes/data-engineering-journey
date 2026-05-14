import pandas as pd

# Checking how big is your data set and {ROW index} name.

df = pd.read_csv("Library/Pandas/employe.csv")

print(f"\n Row-Col-Value: {df.shape}")
print(f"\n Col-Name: {df.columns} \n")


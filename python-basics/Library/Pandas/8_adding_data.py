import pandas as pd

df = pd.read_csv("Library/Pandas/employe.csv")

df["Bonus"] = df["Salary"]*0.1
print("\nNow add bonus in data\n")
print(df)

# Using insert() method how to add additional data.

df.insert(0,"Id",[10,20,30,40,50,60,70,80,90,100])
print(df)
 
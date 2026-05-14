import pandas as pd

df = pd.read_csv("Library/Pandas/friends.csv")

dff = pd.read_csv("Library/Pandas/customers.csv")

print("Name of friend:\n")
print(df)           # top two value output

# print("Name of data:\n")
# print(df.tail(2))            # down two valut output

print(df.info())             # All over surmise-Value

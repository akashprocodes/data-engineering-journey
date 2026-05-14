import pandas as pd

dff = pd.read_csv("Library/Pandas/customers.csv")

print("Display info for customer data")
print(dff.info())
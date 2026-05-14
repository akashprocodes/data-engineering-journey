import pandas as pd

df = pd.read_csv("Library/Pandas/employe.csv")

print("Value of employee \n")
print(df)

name = df['Name']
print(f"Single Name column \n{name}")

multiplu = df[['Name', 'Salary']]
print(f"multiple Name & Salary column \n{multiplu}")
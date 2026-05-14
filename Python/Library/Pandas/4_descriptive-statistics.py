import pandas as pd 

df = pd.read_csv("Library/Pandas/employe.csv")

print("Value befor Descriptive \n")
print(df)


print("Value After Descriptive \n")
print(df.describe())



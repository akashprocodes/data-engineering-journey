import pandas as pd

ab = pd.read_csv("Library/Pandas/employe.csv")

#Single condtion base filter output

hight_salary = ab[ab['Salary']>50000]
print("\n Employee list Salary > 50000 \n")
print(hight_salary)

#Multiple condition base filter output

age_and_salary = ab[(ab['Age'] > 25) & (ab['Salary'] > 50000)] 
print("\n Employee list Age > 30 & Salary > 50000 \n")
print(age_and_salary)
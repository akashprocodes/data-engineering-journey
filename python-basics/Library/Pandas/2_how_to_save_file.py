import pandas as pd

Data = {

    "Name":["Akash", "Sneha" ,"sid", "Rahul", "Niraj",],
    "Age": [23, 20, 25, 25, 22],
    "City": ["Jamui", "Jamaalpur", "Shekpura", "Patna", "Sono"]
}

df = pd.DataFrame(Data)
print(df)

df.to_csv("friends.csv", index=False) # This program of line save data set of any type like : CSV, JSON, EXCEL
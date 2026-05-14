from utils import check_adult, check_high_income

user_data = {
    "name": "Akash",
    "age": 24,
    "salary": 50000
}

is_adult = check_adult(user_data["age"])
is_high_income = check_high_income(user_data["salary"])

print("User:", user_data["name"])
print("Adult:", is_adult)
print("High Income:", is_high_income)
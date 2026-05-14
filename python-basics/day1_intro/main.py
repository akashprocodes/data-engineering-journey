# Raw Data (simulate real-world input)
user_data = {
    "name": "Akash",
    "age": 24,
    "salary": 50000
}

# Processing (business logic)
is_adult = user_data["age"] >= 18
is_high_income = user_data["salary"] > 30000

# Output (system result)
print("User:", user_data["name"])
print("Adult:", is_adult)
print("High Income:", is_high_income)
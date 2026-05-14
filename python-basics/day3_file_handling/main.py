import csv

with open ("python-basics/day3_file_handling/data.csv", "r") as file:
    reader = csv.DictReader(file)

    processed_data = []

    for row in reader:

        age = int(row["age"])
        salary = int(row["salary"])

        row["is_adult"] = age >= 18
        row["is_high_income"] = salary > 30000
        row["category"] = "high" if salary > 50000 else "Low"

        processed_data.append(row)

with open("python-basics/day3_file_handling/output.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "salary", "category", "is_adult", "is_high_income"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(processed_data)

print("ETL Process Completed ✅")
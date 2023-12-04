from statistics import mean, mode, multimode
from collections import defaultdict

def calculate_bmi(height, weight):
    return weight / (height ** 2)

def store_bmi_data(bmi_records, height, weight, age):
    bmi = calculate_bmi(height, weight)
    bmi_data = {
        "Height": height,
        "Weight": weight,
        "Age": age,
        "BMI": bmi
    }
    bmi_records.append(bmi_data)

def calculate_statistics(bmi_records):
    stats = defaultdict(dict)
    transposed_data = {
        "Height": [record["Height"] for record in bmi_records],
        "Weight": [record["Weight"] for record in bmi_records],
        "Age": [record["Age"] for record in bmi_records],
        "BMI": [record["BMI"] for record in bmi_records]
    }

    for key in transposed_data:
        stats[key]["Mean"] = mean(transposed_data[key])
        try:
            stats[key]["Mode"] = mode(transposed_data[key])
        except:
            stats[key]["Mode"] = multimode(transposed_data[key])
        stats[key]["Range"] = max(transposed_data[key]) - min(transposed_data[key])

    return stats


# Storing data for multiple users using user input
bmi_records = []

while True:
    # User input for Height, Weight, and Age
    try:
        height = float(input("Enter height in meters: "))
        weight = float(input("Enter weight in kilograms: "))
        age = int(input("Enter age in years: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    store_bmi_data(bmi_records, height, weight, age)

    # Check if the user wants to add more data
    add_more = input("Do you want to add more data? (yes/no): ").lower()
    if add_more != "yes":
        break

# Calculating statistics
statistics = calculate_statistics(bmi_records)

# Printing the data and statistics
print("Stored BMI Data:")
for i, record in enumerate(bmi_records, 1):
    print(f"User {i}: {record}")

print("\nStatistics:")
for key, value in statistics.items():
    print(f"{key}: {value}")
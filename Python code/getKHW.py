
import csv


# Initialize lists to store the data
khw = []



# Read data from the CSV file : https://www.renewables.ninja/
with open('/home/neo/Downloads/Tekno-Catalay-2024/Mathlab code/Load_profile_10 (1).xlsx - Load Profiles.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.DictReader(file)

    for row in reader:

        khw.append(row['kWh'])

    print(khw)

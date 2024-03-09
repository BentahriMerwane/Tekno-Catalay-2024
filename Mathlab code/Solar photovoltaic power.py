import matplotlib.pyplot as plt
import csv
from datetime import datetime

# Initialize lists to store the data
dates = []
data_values = []

# Read data from the CSV file : https://www.renewables.ninja/
with open('/home/neo/Downloads/Tekno-Catalay-2024/Mathlab code/kwhwallon.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file, delimiter=',')
    
    # Skip the header row
    next(reader)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Convert the date string to datetime object
        date = datetime.strptime(row[1], "%Y-%m-%d %H:%M")
        dates.append(date)  # Append date to the list
        data_values.append(float(row[-1]))  # Assuming the last column contains the values

# Plot the data
plt.plot(dates, data_values)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Results: Solar photovoltaic power (PV)')
plt.grid(True)
plt.show()

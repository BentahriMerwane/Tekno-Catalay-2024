import matplotlib.pyplot as plt
import csv
from datetime import datetime
from matplotlib.dates import DateFormatter

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
plt.figure(figsize=(10, 6))  # Adjust figure size
plt.plot(dates, data_values) 
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Results: Solar photovoltaic power (PV) (https://www.renewables.ninja/)')
 # Add markers and customize color
# Customize date format on x-axis
date_form = DateFormatter("%Y-%m-%d")
plt.gca().xaxis.set_major_formatter(date_form)
plt.gcf().autofmt_xdate()  # Rotate x-axis labels for better readability

plt.grid(True)
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.savefig('spp.png')
plt.show()

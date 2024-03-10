import matplotlib.pyplot as plt
import csv
from datetime import datetime
from matplotlib.dates import DateFormatter
from matplotlib.animation import FuncAnimation

# Initialize lists to store the data
dates = []
data_values = []

# Read data from the CSV file
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

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the initial data
line, = ax.plot(dates, data_values)
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.set_title('Results: Solar photovoltaic power (PV)')

# Customize date format on x-axis
date_form = DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(date_form)
fig.autofmt_xdate()  # Rotate x-axis labels for better readability

ax.grid(True)
plt.tight_layout()  # Adjust layout to prevent clipping of labels

# Function to update the plot data for animation
def animate(i):
    line.set_data(dates[:i], data_values[:i])  # Update data up to index i
    return line,

# Create animation
ani = FuncAnimation(fig, animate, frames=len(dates), interval=0.1, blit=True)

# Show the animation
plt.show()

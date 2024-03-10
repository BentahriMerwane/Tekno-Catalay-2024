import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from scipy.io import loadmat
from matplotlib.animation import FuncAnimation

# Load MATLAB data
irradpv = loadmat('/home/neo/Downloads/Tekno-Catalay-2024/Mathlab code/irraddatapv.mat')

# Accessing variables from irradpv
MinirradSf = irradpv['Minirrad']  # irradiance on Panel each minute

# Fit a smooth curve using spline interpolation
spline = UnivariateSpline(range(irradpv['j'][0, 0]), MinirradSf[0, :])

# Create a figure and axis object
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

# Set up the plot properties
ax.set_xlim(0, len(MinirradSf[0, :]))
ax.set_ylim(0, np.max(MinirradSf) * 1.1)
ax.set_xlabel('Time (minutes)')
ax.set_ylabel('Irradiance on Panel (W/m^2)')
ax.set_title('Smooth Curve of Irradiance on Panel vs. Time')
ax.grid(True)

# Function to update the plot data for animation
def animate(i):
    x = range(i)
    y = spline(x)
    line.set_data(x, y)
    return line,

# Create animation
ani = FuncAnimation(fig, animate, frames=len(MinirradSf[0, :]), interval=0.1, blit=True)

# Show the animation
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from scipy.io import loadmat
# Load MATLAB data
irradpv = loadmat('/home/neo/Downloads/Tekno-Catalay-2024/Mathlab code/irraddatapv.mat')

# Accessing variables from irradpv
di = irradpv['di']  # Diffusive irradiance
globi = irradpv['globi']  # Global irradiance

# Sample data generation for demonstration
np.random.seed(0)

l = irradpv['l']  # local Latitude
Lst = irradpv['Lst']  # standard longitude for the time zone
Lloc = irradpv['Lloc']  # local longitude
Ea = irradpv['Ea']  # extraterrestrial irradiance

sunalt = irradpv['sunalt']  # altitude sun angle
anginc = irradpv['anginc']  # angle of incidence

tilt = irradpv['tilt']  # tilt angle
modazy = irradpv['modazy']  # module azimuth angle

DHI = irradpv['DHI']  # diffusive matrix data
GHI = irradpv['GHI']  # global mat data
DNI = irradpv['DNI']  # normal mat data
MinirradSf = irradpv['Minirrad']  # irradiance on Panel each minute

# Fit a smooth curve using spline interpolation
spline = UnivariateSpline(range(irradpv['j'][0, 0]), MinirradSf[0, :])

# Plot the smooth curve
plt.plot(range(irradpv['j'][0, 0]), spline(range(irradpv['j'][0, 0])))
plt.xlabel('Time (minutes)')
plt.ylabel('Irradiance on Panel (W/m^2)')
plt.title('Smooth Curve of Irradiance on Panel vs. Time')
plt.grid(True)
plt.show()

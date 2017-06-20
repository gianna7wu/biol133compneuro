# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Import the data file
X=np.loadtxt('lab10d.tsv')
#period 
T = 4.510115
# Extract the data from the array
#time
x0=X[:,0]
#interval
x1=X[:,1]


# Plot the data in the form of a figure

def func(x, phi):
    return phi / T - (x / T)

phi = x0 / T
y = func(x1, phi)
plt.plot(x0, y, 'b-')
# pNew = phi / T - (x1/T)
plt.plot(x0, -0.15 - 0.2*np.sin(2*np.pi*phi + 1.75*np.pi), 'r-', linewidth=2)
# plt.plot(x0, pNew,'r-', linewidth=2)
popt, pcov = curve_fit(func, x0, y)
plt.plot(x0, func(x1, *popt) - 3.1, 'g-')

#for the PRC
# plt.plot(x0, 1 - (x1 / T),'k-',linewidth=2)

plt.xlabel('X',fontsize=16)
plt.ylabel('Y',fontsize=16)

# Save the figure in an appropriate format
# plt.savefig('spiral.png',dpi=600)
# plt.savefig('spiral.eps',dpi=600)

# Show the figure on the compter screen
plt.show()

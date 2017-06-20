# Import the required packages
import numpy as np
import matplotlib.pyplot as plt

# Import the data file
X=np.loadtxt('spiral.tsv')

# Extract the data from the array
x0=X[:,0]
x1=X[:,1]
x2=X[:,2]

# Plot the data in the form of a figure
plt.plot(x1,x2,'k-',linewidth=2)
plt.xlabel('X',fontsize=16)
plt.ylabel('Y',fontsize=16)

# Save the figure in an appropriate format
plt.savefig('spiral.png',dpi=600)
plt.savefig('spiral.eps',dpi=600)

# Show the figure on the compter screen
plt.show()

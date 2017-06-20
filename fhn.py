import pylab as plt
import numpy as np
import scipy.integrate as integrate

# Initial setup
a = 0.25
b = 4
c = 0.1
I = 0.25
t = np.linspace(0, 100, 1000, endpoint = True)


# Equations
def dx(x, y):
	return x*(a-x)*(x-1)- y + I

def dy(x,y):
	return b*x - c*y

# Define derivs() function for second-oder differential equation
def derivs(state, t):
	x,y = state
	deltax = dx(x,y)
	deltay = dy(x,y)
	return deltax, deltay

x0 = 5.0
y0 = 5.0
z0 = [x0, y0]
z = integrate.odeint(derivs, z0, t)

# Gives array with two columns corresponding to x, y respectively
x = z[:,0]
y = z[:,1]

# #make a direction field plot with quiver
# xmax = 1.1 * x.max()
# ymax = 1.1 * y.max()
# X, Y = np.meshgrid(np.arange(-1, xmax), np.arange(-1, ymax))
# dX = dx(X, Y)
# dY = dy(X, Y)
# plt.quiver(X, Y, dX, dY)

# X, Y = np.meshgrid(np.arange(-4, xmax, .1), np.arange(-4, ymax, .1))
dX = dx(x, y)
dY = dy(x, y)

# plt.contour(X, Y, dX, levels=[0])
# plt.contour(X, Y, dY, levels=[0])

#Plots x vs. t
# plt.plot(t, x, 'k-')
#
# #Plots y vs. t
# plt.plot(t, y, 'k-')

# Plots phase plane
plt.plot(x,y, 'k-')
plt.show()

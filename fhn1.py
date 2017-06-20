import pylab as plt
import numpy as np
import scipy.integrate as integrate


a = 0.25
b = 3.0
c = 0.9
I0 = 0.0
t = np.linspace(0, 10, 10000, endpoint = True)
w = np.linspace(-2, 2, 1000, endpoint = True)
u = np.linspace(-2, 2, 1000, endpoint = True)

def dx(x, y):
	return x*(a-x)*(x-1)- y + I0

def dy(x,y):
	return b*x - c*y

def derivs(state, t):
	x,y = state
	deltax = dx(x,y)
	deltay = dy(x,y)
	return deltax, deltay

x0 = 5.0
y0 = 5.0
z0 = [x0,y0]
z = integrate.odeint(derivs, z0, t)

x = z[:,0]
y = z[:,1]

# Equations



v = w*(a-w)*(w-1)
m = b / c * u

plt.subplot(311)
plt.axis([-2, 2, -1, 1])
plt.plot(w,v, 'k-')
plt.plot(u,m, 'k--')
plt.plot(x,y, 'r-')


a = 0.25
b = 0.0
c = 4
I1 = 0.0

t = np.linspace(0, 10, 10000, endpoint = True)
w = np.linspace(-2, 2, 1000, endpoint = True)
u = np.linspace(-2, 2, 1000, endpoint = True)

def dx(x, y):
	return x*(a-x)*(x-1)- y + I1

def dy(x,y):
	return b*x - c*y

def derivs(state, t):
	x,y = state
	deltax = dx(x,y)
	deltay = dy(x,y)
	return deltax, deltay

x0 = 5.0
y0 = 5.0
z0 = [x0,y0]
z = integrate.odeint(derivs, z0, t)

x = z[:,0]
y = z[:,1]

# Equations



v = w*(a-w)*(w-1)
m = b / c * u
#
plt.subplot(312)
plt.axis([0.9, 1.1, -0.25, 0.25])
plt.plot(w,v, 'k-')
plt.plot(u,m, 'k--')
plt.plot(x,y, 'r-')




a = 0.25
b = 4.0
c = 1.0
I2 = 1.0

# a = 0.25
# b = 3.0
# c = 0.9
# I2 = 0.0

t = np.linspace(0, 10, 10000, endpoint = True)
w = np.linspace(-2, 2, 1000, endpoint = True)
u = np.linspace(-2, 2, 1000, endpoint = True)

def dx(x, y):
	return x*(a-x)*(x-1)- y + I2

def dy(x,y):
	return b*x - c*y

def derivs(state, t):
	x,y = state
	deltax = dx(x,y)
	deltay = dy(x,y)
	return deltax, deltay

x0 = 5.0
y0 = 5.0
z0 = [x0,y0]
z = integrate.odeint(derivs, z0, t)

x = z[:,0]
y = z[:,1]

# Equations



v = w*(a-w)*(w-1)
m = b / c * u
#
plt.subplot(313)
plt.axis([-3, 3, -3, 3])
plt.plot(w,v, 'k-')
plt.plot(u,m, 'k--')
plt.plot(x,y, 'r-')

plt.show()

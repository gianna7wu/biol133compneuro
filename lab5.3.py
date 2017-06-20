import pylab as plt
import numpy as np
import scipy.integrate as integrate
e=0.1
a=0
t=np.linspace(0, 10, 100, endpoint=True)
#
# Define deriv() for second-order differential equation
def derivs(state,t):
    x,y = state
    deltax = y
    deltay = e*(a-x**2)*y - x
    return deltax,deltay
x0=1.0
y0=0.0
z0=[x0, y0]
z=integrate.odeint(derivs, z0, t)
#
# Output is the array z[] containing two columns
# First column is 0 and contains x
# Second column is 1 and contains y
#
x=z[:,0]
y=z[:,1]
#
# plot x versus time
# plt.plot(t,x,'k-')
#
# plot y versus time
# plt.plot(t,y,'k-')
#
# plot phase plane
#
plt.plot(x,y,'k-')

e=0.1
a=6
t=np.linspace(0, 10, 100, endpoint=True)
#
# Define deriv() for second-order differential equation
def derivs(state,t):
    x,y = state
    deltax = y
    deltay = e*(a-x**2)*y - x
    return deltax,deltay
x0=1.0
y0=0.0
z0=[x0, y0]
z=integrate.odeint(derivs, z0, t)
#
# Output is the array z[] containing two columns
# First column is 0 and contains x
# Second column is 1 and contains y
#
x=z[:,0]
y=z[:,1]
#
# plot x versus time
# plt.plot(t,x,'k-')
#
# plot y versus time
# plt.plot(t,y,'k-')
#
# plot phase plane
#
plt.plot(x,y,'k--')


e=0.1
a=13.2
t=np.linspace(0, 10, 100, endpoint=True)
#
# Define deriv() for second-order differential equation
def derivs(state,t):
    x,y = state
    deltax = y
    deltay = e*(a-x**2)*y - x
    return deltax,deltay
x0=1.0
y0=0.0
z0=[x0, y0]
z=integrate.odeint(derivs, z0, t)
#
# Output is the array z[] containing two columns
# First column is 0 and contains x
# Second column is 1 and contains y
#
x=z[:,0]
y=z[:,1]
#
# plot x versus time
# plt.plot(t,x,'k-')
#
# plot y versus time
# plt.plot(t,y,'k-')
#
# plot phase plane
#
plt.plot(x,y,'k-.')

plt.show()

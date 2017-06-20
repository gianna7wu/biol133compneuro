import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

f=1.0/7.0
N=10000
a=1
k1=-3
k2=-8
start=0.0
stop=200.0

t=np.linspace(start,stop,num=N,endpoint=True)

def derivs(state,t):
    x,y=state
    deltax=y
    deltay=a*np.sin(2.0*np.pi*f*t)-k1*y-k2*x
    return deltax,deltay

x0=5.0
y0=0.0
z0=[x0,y0]
z=integrate.odeint(derivs,z0,y0)

plt.plot(t,np.sin(2*np.pi*f*t),'k')
plt.axis([0,stop,-1.1,1.1])
plt.show()

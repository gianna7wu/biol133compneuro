import pylab as plt
import numpy as np
import scipy.integrate as integrate


#amplitude = 1
#change stop if you change frequency
#do convolutions, frequency, automatic something l0l
start=0.0
stop=1000
k=-1
N=100000
f=0.01
#for the phase, plot the sin curve on the same plot
t=np.linspace(start,stop,num=N,endpoint=True)

def dx(x,t,):
	return k*x + np.sin(2*np.pi*f*t)

x0 = 5.0
t0 = 0.0
z0 = [x0]
z = integrate.odeint(dx, z0, t)


plt.plot(t,z,'k-o')
plt.axis([0,stop,-1.1,1.1])
plt.show()

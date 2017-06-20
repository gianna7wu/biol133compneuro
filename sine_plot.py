import numpy as np
import matplotlib.pyplot as plt

f=0.1
N=11
NN=101
start=0.0
stop=100.0
dt=10

t=np.linspace(start,stop,num=N,endpoint=True)
tt=np.linspace(start,stop,num=NN,endpoint=True)

plt.plot(t,np.sin(2*np.pi*f*t),'k-o')
plt.plot(tt,np.sin(2*np.pi*f*tt),'r-')

plt.axis([0,stop,-1.1,1.1])

plt.show()

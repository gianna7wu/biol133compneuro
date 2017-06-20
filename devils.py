import numpy as np
import pylab as plt


k=0.2

pb=np.zeros(200)
ppb=np.zeros(200)

def f(b):
    i=0
    x=np.zeros(500)
    x[0]=4.896183
    while i < 499:
        # x[i+1]=(x[i]+b+k*np.sin(2.*np.pi*x[i]))
        x[i+1]=(x[i] + b + k*np.sin(2.*np.pi*x[i] + 1.75*np.pi))
        i=i+1
    return x[499]

j=0
while j<200:
    pb[j]=f(0.005*j)
    ppb[j]=0.005*j
    j=j+1

plt.plot(ppb,pb/500.0,'k-',linewidth=2)

plt.axis([-0.05,1.05,-0.05,1.05])

plt.ylabel('Rotation number',fontsize=18)
plt.xlabel('b',fontsize=18)


plt.show()

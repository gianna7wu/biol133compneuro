import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(-np.pi,np.pi,1000)

#sum = 0.5
#n=1

def gibb(nn):
    sum =0.5
    n=1
    while n < nn:
        sum = sum + np.divide(2,(2*n-1)*np.pi)*np.sin((2*n-1)*t)
        n=n+1
    return sum


plt.plot(t,gibb(5))
plt.plot(t,gibb(25),'k-')
plt.plot(t,gibb(50),'r-')


plt.show()  

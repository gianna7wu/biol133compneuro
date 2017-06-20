import pylab as plt
import numpy as np
import matplotlib.ticker as ticker

t=np.linspace(-np.pi,np.pi,1000)
def gibbs(k):
    n=1
    sum=0.5
    while n<k:
        sum=sum+np.divide(2,(2*n-1)*np.pi)*np.sin((2*n-1)*t)
        n=n+1
    return sum


def plotGibbs(k):
    plt.plot(t,np.sin(t),'co')
    plt.plot(t,gibbs(k*0.2),'k-')
    plt.plot(t,gibbs(k*0.5),'b-')
    plt.plot(t,gibbs(2*k),'m-')
    plt.plot(t,gibbs(2*k),'g-')
    plt.plot(t,gibbs(4*k),'r-')
    plt.show()

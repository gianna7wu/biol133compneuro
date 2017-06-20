import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

t = np.linspace(-np.pi, np.pi, 1000, endpoint=True)

def g(x):
    sum=0.5
    n = 1
    while n < x:
        sum=sum + ((2/((2*n - 1)*np.pi))*(np.sin((2*n - 1)*t)))
        n=n+1
    return sum

x=(0.5*signal.square(t)) + 0.5

plt.plot(t, g(5), 'k-')
plt.plot(t, g(100), 'k-')
plt.plot(t, (0.5*np.sin(t)) + 0.5, 'b-')
plt.plot(t, g(10), 'k-')

plt.plot(t, x, 'r-')

plt.show()

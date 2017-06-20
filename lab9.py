import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

#import matplotlib
#Nyquist frequency is 32

#f1, f2 values for example
# f1 = 4.0
# f2 = 50.0

f1 = 10.0;
f2 = 45.0; 

t=np.arange(0,100,0.015625)

#xt=np.sin(2*np.pi*t)
yt=np.sin(2.0*np.pi*f1*t)+np.sin(2.0*np.pi*f2*t)
power,freqs=mlab.psd(yt,len(yt),64,pad_to=10192)
#print len(xt)
plt.plot(freqs,power)
plt.show()

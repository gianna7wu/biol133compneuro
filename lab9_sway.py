import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft
import matplotlib.mlab as mlab


#data sampled at 200 Hz
# data=np.loadtxt('sway_new.csv', delimiter=',')
data=np.loadtxt('fish_1s_10000.tsv')
x = data[:,0]
y = data[:,1]

X = np.sqrt(x**2 + y**2);

power,freqs=mlab.psd(X, 10000,10000)
# plt.plot(X)
plt.plot(freqs,20*np.log10(power))
plt.show()

import pylab as plt
import numpy as np
import scipy.signal as signal
import matplotlib.ticker as ticker

tt=np.arange(48000,50000,1)
t=np.linspace(0,100,50000)
x=0.5*signal.square(2*np.pi*5.0*t)
dt=0.002


k=0.18
def impulse_response(t):
    return (k*np.exp(-k*t))

kk=0.18

def second_impulse(t):
     return (kk*np.exp(-kk*t))

Nt=len(t)

r=impulse_response(t)

rr=second_impulse(t)

z=np.convolve(x,r,mode='full')

zz=z[:Nt]
print np.shape(zz)
print len(zz)

w=np.convolve(z,r,mode='full')
ww=w[:Nt]

ax=plt.subplot(311)
plt.plot(x,'k-',linewidth=2)
plt.axis([48000,50000,-1.5,1.5])
ax.xaxis.set_major_locator(ticker.NullLocator())
#ax.yaxis.set_major_locator(ticker.NullLocator())
plt.title('INPUT',fontsize=16)

bx=plt.subplot(312)
plt.plot(dt*zz,'k-',linewidth=2)
plt.axis([48000,50000,-.1,.1])
bx.xaxis.set_major_locator(ticker.NullLocator())
#bx.yaxis.set_major_locator(ticker.NullLocator())
plt.title('FIRST LOW-PASS FILTER',fontsize=16)

cx=plt.subplot(313)
plt.plot(dt*ww,'k-',linewidth=2)
plt.axis([48000,50000,-.1,.1])
cx.xaxis.set_major_locator(ticker.NullLocator())
#cx.yaxis.set_major_locator(ticker.NullLocator())
plt.xlabel('TIME',fontsize=18)
plt.title('SECOND LOW-PASS FILTER',fontsize=16)



#plt.savefig('square_sine.png',dpi=600)
#plt.savefig('square_sine.eps',dpi=600)




plt.show()

import numpy as np
import pylab as plt

import numpy.linalg as linalg

X1=np.matrix(np.random.rand(2,3000))-0.5
#name = 'saddle'
sx, sy, angle = 0, 0, 6.5
theta = angle*np.pi/180.
S1 = np.matrix([[sx, 0],
            [0, sy]])
R = np.matrix([[np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)],])
M = S1*R
print M
print R
vals, vecs = linalg.eig(M)
print vals
X2=M*X1
ax=plt.subplot(111)
x1=X1[0].flat
y1=X1[1].flat
x2=X2[0].flat
y2=X2[1].flat
line1,line2 = plt.plot(x1, y1, 'ko', x2, y2, 'ro', markersize=2.5)
plt.show()

from matplotlib import pyplot as plt
import numpy as np

P1 = np.array([2,2])
P2 = np.array([10,3])
M1 = np.array([3,-3])
M2 = np.array([0,-5])

t=0

while t<=1:
    a = 2*t*t*t-3*t*t+1
    b = t*t*t-2*t*t+t
    c = -2*t*t*t+3*t*t
    d = t*t*t-t*t

    P = a*P1 + b*M1 + c*P2 + d*M2
    plt.scatter(P[0],P[1])
    t+=0.01

plt.show()

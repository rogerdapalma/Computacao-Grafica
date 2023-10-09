from matplotlib import pyplot as plt
import numpy as np

P0 = np.array([2,2])
P1 = np.array([3,5])
P2 = np.array([-4,-6])
P3 = np.array([10,6])

t=0
while t<=1:
    a = (1-t)*(1-t)*(1-t)
    b = 3*(1-t)*(1-t)*t
    c = 3*(1-t)*t*t
    d = t*t*t

    P = a*P0 + b*P1 + c*P2 + d*P3
    plt.scatter(P[0], P[1])
    t+=0.01

plt.show()
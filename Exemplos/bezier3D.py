from matplotlib import pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

P0 = np.array([2,2,1])
P1 = np.array([3,5,2])
P2 = np.array([-4,-6,3])
P3 = np.array([10,6,4])

t=0
while t<=1:
    a = (1-t)*(1-t)*(1-t)
    b = 3*(1-t)*(1-t)*t
    c = 3*(1-t)*t*t
    d = t*t*t

    P = a*P0 + b*P1 + c*P2 + d*P3
    ax.scatter(P[0], P[1], P[2])
    t+=0.01

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title("Curva de Bezier 3D")

plt.show()
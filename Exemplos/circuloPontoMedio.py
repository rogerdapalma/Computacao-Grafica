import numpy as np
import matplotlib.pyplot as plt
import math

def calculaPontosSimetria(x,y):
    plt.scatter(x,y)
    plt.scatter(x,-y)
    plt.scatter(-x,y)
    plt.scatter(-x,-y)
    plt.scatter(y,x)
    plt.scatter(y,-x)
    plt.scatter(-y,x)
    plt.scatter(-y,-x)

r = 40

x = 0
y = r
calculaPontosSimetria(x,y)

p = 1-r

while x < y:
    if p < 0:
        x+=1
        p = p + 2*x + 1
    elif p >=0:
        x+=1
        y-=1
        p = p + 2*x - 2*y + 1
    calculaPontosSimetria(x,y)
plt.show()
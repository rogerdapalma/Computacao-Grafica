import numpy as np
import matplotlib.pyplot as plt
import math

r = 40
x = 0

plt.xlim(-r*2,r*2)
plt.ylim(-r*2,r*2)

limite = math.cos(math.radians(45))*r
print("limite = ",limite)
while x <= limite:
    y = round(math.sqrt(r*r - x*x))
    plt.scatter(x,y)
    plt.scatter(x,-y)
    plt.scatter(-x,y)
    plt.scatter(-x,-y)
    plt.scatter(y,x)
    plt.scatter(y,-x)
    plt.scatter(-y,x)
    plt.scatter(-y,-x)

    x+=1
plt.show()
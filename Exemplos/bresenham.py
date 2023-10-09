import matplotlib.pyplot as plt
import numpy as np

p1 = np.array([1,1])
p2 = np.array([2,1000])

#verificamos se a reta não está totalmente de pé, na vertical
if p1[0] == p2[0]:
    print("Reta vertical")
    x = p1[0]
    y = p1[1]
    while y <= p2[1]:
        print("(",x,",",y,")")
        y+=1
    
else: #retas não verticais
    Dy = p2[1] - p1[1]
    Dx = p2[0] - p1[0]
    m = (Dy)/(Dx)
    ajuste = 1
    offset = 0

    if m <= 1: #angulo <= 45º
        print("Reta mais deitada, x cresce mais que y")
        delta = Dy*2
        limiar = Dx
        limiarInc= Dx*2
        x = p1[0]
        y = p1[1]
        while x <= p2[0]: 
            print("(",x,",",y,")")
            plt.scatter(x,y)
            offset+=delta
            if offset >= limiar:
                y+=ajuste
                limiar+=limiarInc
            x+=1

    elif m > 1: #angulo > 45º
        print("Reta mais de pé, y cresce mais que x")
        delta = Dx*2
        limiar = Dy
        limiarInc= Dy*2
        x = p1[0]
        y = p1[1]
        while y <= p2[1]: 
            print("(",x,",",y,")")
            plt.scatter(x,y)
            offset+=delta
            if offset >= limiar:
                x+=ajuste
                limiar+=limiarInc
            y+=1

plt.show()#abre a janela
import matplotlib.pyplot as plt
import numpy as np

p1 = np.array([2,1])
p2 = np.array([2,8])

#verificamos se a reta não está totalmente de pé, na vertical
if p1[0] == p2[0]:
    print("Reta vertical")
    x = p1[0]
    y = p1[1]
    while y <= p2[1]:
        print("(",x,",",y,")")
        y+=1
    
else: #retas não verticais
    m = (p2[1] - p1[1])/(p2[0] - p1[0]) #(y2-y1)/(x2-x1)
    b = p1[1] - m * p1[0] #y1 - m*x1
    print("Equação: y=",m,",x + ",b)

    if m <= 1: #angulo <= 45º
        print("Reta mais deitada, x cresce mais que y")
        x = p1[0] # x começa em 2
        while x <= p2[0]: #x vai até 8
            y = round(m*x + b)
            print("(",x,",",y,")")
            plt.scatter(x,y) #renderiza na tela os pixeis
            x+=1

    elif m > 1: #angulo > 45º
        print("Reta mais de pé, y cresce mais que x")
        y = p1[1]
        while y <= p2[1]:
            x = round((y-b)/m)
            print("(",x,",",y,")")
            plt.scatter(x,y) #renderiza na tela os pixeis
            y+=1

plt.show()#abre a janela
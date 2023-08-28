import matplotlib.pyplot as plt
import numpy as np

p1 = np.array([2,1])
p2 = np.array([5,7])

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
    #x e y começam com os valores do ponto inicial da reta
    x = p1[0]
    y = p1[1]

    if m <= 1: #angulo <= 45º
        print("Reta mais deitada, x cresce mais que y")
        while x <= p2[0]: #x vai até 8
            yRound = round(y)
            print("(",x,",",yRound,")")
            plt.scatter(x,yRound) #renderiza na tela os pixeis
            x+=1
            y+=m

    elif m > 1: #angulo > 45º
        print("Reta mais de pé, y cresce mais que x")
        while y <= p2[1]:
            xRound = round(x)
            print("(",xRound,",",y,")")
            plt.scatter(xRound,y) #renderiza na tela os pixeis
            x+=(1/m)
            y+=1

plt.show()#abre a janela
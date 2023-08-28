import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter

#teste de desempenho para retas mais deitadas 
tini = perf_counter()

i = 0

while i < 1000:
    p1 = np.array([2,1])
    p2 = np.array([9000,3000])
    #algoritmo natural
    '''m = (p2[1] - p1[1])/(p2[0] - p1[0]) #(y2-y1)/(x2-x1)
    b = p1[1] - m * p1[0] #y1 - m*x1

    x = p1[0] # x começa em 2
    while x <= p2[0]: #x vai até 8
        y = round(m*x + b)
        x+=1'''
    

    #algoritmo DDA
    '''x = p1[0]
    y = p1[1]
    m = (p2[1] - p1[1])/(p2[0] - p1[0]) #(y2-y1)/(x2-x1)
    while x <= p2[0]: #x vai até 8
        yRound = round(y)
        x+=1
        y+=m'''
    
    #algoritmo bresenham
    Dy = p2[1] - p1[1]
    Dx = p2[0] - p1[0]
    m = (Dy)/(Dx)
    ajuste = 1
    offset = 0
    delta = Dy*2
    limiar = Dx
    limiarInc= Dx*2
    x = p1[0]
    y = p1[1]
    while x <= p2[0]: 
        offset+=delta
        if offset >= limiar:
            y+=ajuste
            limiar+=limiarInc
        x+=1
    
    i+=1

tfim = perf_counter()
print(tfim-tini)
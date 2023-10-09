import numpy as np
import matplotlib.pyplot as plt
import math
from time import perf_counter

r = 40

def circuloNatual(r):
    x = 0
    limite = math.cos(math.radians(45))*r
    while x <= limite:
        y = round(math.sqrt(r*r - x*x))
        (x,y)
        (x,-y)
        (-x,y)
        (-x,-y)
        (y,x)
        (y,-x)
        (-y,x)
        (-y,-x)
        x+=1

def circuloPontoMedio(r):
    x = 0
    y = r
    p = 1-r
    while x < y:
        if p < 0:
            x+=1
            p = p + 2*x + 1
        elif p >=0:
            x+=1
            y-=1
            p = p + 2*x - 2*y + 1
        (x,y)
        (x,-y)
        (-x,y)
        (-x,-y)
        (y,x)
        (y,-x)
        (-y,x)
        (-y,-x)

tempoTotal = 0

for i in range(10):
    tini = perf_counter()
    circuloPontoMedio(400000)
    tfim = perf_counter()
    tempoTotal+=tfim-tini

tempoTotal/=10
print("Tempo médio = ",tempoTotal)
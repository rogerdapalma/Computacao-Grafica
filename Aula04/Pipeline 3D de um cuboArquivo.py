
import numpy as np
import math
import matplotlib.pyplot as plt

#limites da window
xminw = -5
yminw = -5
xmaxw = 0
ymaxw = 0

#limites da viewport
xminv = 0
yminv = 0
xmaxv = 400
ymaxv = 400

def mostraPontos(p1, p2, p3, p4, p5, p6, p7, p8):
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(p5)
    print(p6)
    print(p7)
    print(p8)

def desenhaLinha(p1x, p1y, p2x, p2y):
    point1 = [p1x, p1y]
    point2 = [p2x, p2y]
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plt.plot(x_values, y_values, 'bo', linestyle="--")

#1) Modelagem do objeto - cubo
p1 = np.array([-0.5,-0.5,-0.5, 1.0])
p2 = np.array([-0.5,-0.5,0.5, 1.0])
p3 = np.array([-0.5,0.5,-0.5, 1.0])
p4 = np.array([-0.5,0.5,0.5, 1.0])
p5 = np.array([0.5,-0.5,-0.5, 1.0])
p6 = np.array([0.5,-0.5,0.5, 1.0])
p7 = np.array([0.5,0.5,-0.5, 1.0])
p8 = np.array([0.5,0.5,0.5, 1.0])
print("\nCoordenadas do modelo")
mostraPontos(p1, p2 ,p3 ,p4 ,p5 ,p6 ,p7 ,p8)

#a. Matriz de transformação do modelo
#translação
tx = 0
ty = 0
tz = 0
translacao = np.array([
    [1, 0, 0, tx],
    [0, 1, 0, ty],
    [0, 0, 1, tz],
    [0, 0, 0, 1]
])

#escala
sx = 1
sy = 1
sz = 1
escala = np.array([
    [sx, 0, 0, 0],
    [0, sy, 0, 0],
    [0, 0, sz, 0],
    [0, 0, 0, 1]
])

#rotacao em x
angx = math.radians(0)
rotx = np.array([
    [1, 0, 0, 0],
    [0, math.cos(angx), -math.sin(angx), 0],
    [0, math.sin(angx), math.cos(angx), 0],
    [0, 0, 0, 1]
])

#rotacao em y
angy = math.radians(45)
roty = np.array([
    [math.cos(angy), 0, math.sin(angy), 0],
    [0, 1, 0, 0],
    [-math.sin(angy), 0, math.cos(angy), 0],
    [0, 0, 0, 1]
])

#rotacao em z
angz = math.radians(0)
rotz = np.array([
    [math.cos(angz), -math.sin(angz), 0, 0],
    [math.sin(angz), math.cos(angz), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

rotacao = rotz.dot(roty.dot(rotx))

matrizModelo = escala.dot(rotacao.dot(translacao))

#2) Coordenadas do mundo
p1u = matrizModelo.dot(p1)
p2u = matrizModelo.dot(p2)
p3u = matrizModelo.dot(p3)
p4u = matrizModelo.dot(p4)
p5u = matrizModelo.dot(p5)
p6u = matrizModelo.dot(p6)
p7u = matrizModelo.dot(p7)
p8u = matrizModelo.dot(p8)
print("\nCoordenadas do mundo")
mostraPontos(p1u, p2u ,p3u ,p4u ,p5u ,p6u ,p7u ,p8u)

#translação da câmera
txCam = 0
tyCam = 0
tzCam = -5
#é a cena que se move em torno da câmera
translacaoCam = np.array([
    [1, 0, 0, -txCam],
    [0, 1, 0, -tyCam],
    [0, 0, 1, -tzCam],
    [0, 0, 0, 1]
])

#rotação da câmera
#rotacao em y
angyCam = 0
angyCam = math.radians(-angyCam)
rotyCam = np.array([
        [math.cos(angyCam), 0, math.sin(angyCam), 0],
        [0, 1, 0, 0],
        [-math.sin(angyCam), 0, math.cos(angyCam), 0],
        [0, 0, 0, 1]
])

matrizVisualizacao = rotyCam.dot(translacaoCam)

#3) Coordenadas de visualização
p1v = matrizVisualizacao.dot(p1u)
p2v = matrizVisualizacao.dot(p2u)
p3v = matrizVisualizacao.dot(p3u)
p4v = matrizVisualizacao.dot(p4u)
p5v = matrizVisualizacao.dot(p5u)
p6v = matrizVisualizacao.dot(p6u)
p7v = matrizVisualizacao.dot(p7u)
p8v = matrizVisualizacao.dot(p8u)
print("\nCoordenadas de visualização")
mostraPontos(p1v, p2v ,p3v ,p4v ,p5v ,p6v ,p7v ,p8v)

#c. Matriz de projeção
#projeção perspectiva
fovy = math.radians(80.0)
aspect = 1.0
zNear = 0.1
zFar = 100

a = 1/(math.tan(fovy/2) * aspect)
b = 1/(math.tan(fovy/2))
c = (zFar+zNear)/(zNear-zFar)
d = (2*(zFar*zNear))/(zNear-zFar)

matrizProjecao = np.array([
    [a, 0, 0, 0],
    [0, b, 0, 0],
    [0, 0, c, d],
    [0, 0, -1, 0]
])

#4) Coordenadas de projeção
p1p = matrizProjecao.dot(p1v)
p2p = matrizProjecao.dot(p2v)
p3p = matrizProjecao.dot(p3v)
p4p = matrizProjecao.dot(p4v)
p5p = matrizProjecao.dot(p5v)
p6p = matrizProjecao.dot(p6v)
p7p = matrizProjecao.dot(p7v)
p8p = matrizProjecao.dot(p8v)

#divide os pontox (x,y,z,w) por w, para que o w volte a ser 1
p1p = p1p/p1p[3]
p2p = p2p/p2p[3]
p3p = p3p/p3p[3]
p4p = p4p/p4p[3]
p5p = p5p/p5p[3]
p6p = p6p/p6p[3]
p7p = p7p/p7p[3]
p8p = p8p/p8p[3]
print("\nCoordenadas de projeção")
mostraPontos(p1p, p2p ,p3p ,p4p ,p5p ,p6p ,p7p ,p8p)

#define os limites da janela onde os pontos serão renderizados
plt.xlim(350, 450)
plt.ylim(350, 450)

#d. Mapeamento
print("\nMapeamento")
p1mx = (((p1p[0] - xminw)*(xmaxv - xminv))/(xmaxw - xminw)) + xminv
p1my = (((p1p[1] - yminw)*(ymaxv - yminv))/(ymaxw - yminw)) + yminv
p2mx = (((p2p[0] - xminw)*(xmaxv - xminv))/(xmaxw - xminw)) + xminv
p2my = (((p2p[1] - yminw)*(ymaxv - yminv))/(ymaxw - yminw)) + yminv
p3mx = (((p3p[0] - xminw)*(xmaxv - xminv))/(xmaxw - xminw)) + xminv
p3my = (((p3p[1] - yminw)*(ymaxv - yminv))/(ymaxw - yminw)) + yminv
p4mx = (((p4p[0] - xminw)*(xmaxv - xminv))/(xmaxw - xminw)) + xminv
p4my = (((p4p[1] - yminw)*(ymaxv - yminv))/(ymaxw - yminw)) + yminv
p5mx = (((p5p[0] - xminw)*(xmaxv - xminv))/(xmaxw - xminw)) + xminv
p5my = (((p5p[1] - yminw)*(ymaxv - yminv))/(ymaxw - yminw)) + yminv
p6mx = (((p6p[0] - xminw)*(xmaxv - xminv))/(xmaxw - xminw)) + xminv
p6my = (((p6p[1] - yminw)*(ymaxv - yminv))/(ymaxw - yminw)) + yminv
p7mx = (((p7p[0] - xminw)*(xmaxv - xminv))/(xmaxw - xminw)) + xminv
p7my = (((p7p[1] - yminw)*(ymaxv - yminv))/(ymaxw - yminw)) + yminv
p8mx = (((p8p[0] - xminw)*(xmaxv - xminv))/(xmaxw - xminw)) + xminv
p8my = (((p8p[1] - yminw)*(ymaxv - yminv))/(ymaxw - yminw)) + yminv
print(p1mx,",",p1my)
print(p2mx,",",p2my)
print(p3mx,",",p3my)
print(p4mx,",",p4my)
print(p5mx,",",p5my)
print(p6mx,",",p6my)
print(p7mx,",",p7my)
print(p8mx,",",p8my)

#desenha as linhas que formam o cubo
desenhaLinha(p1mx, p1my, p2mx, p2my )
desenhaLinha(p1mx, p1my, p3mx, p3my )
desenhaLinha(p1mx, p1my, p5mx, p5my )

desenhaLinha(p2mx, p2my, p4mx, p4my )
desenhaLinha(p2mx, p2my, p6mx, p6my )

desenhaLinha(p3mx, p3my, p4mx, p4my )
desenhaLinha(p3mx, p3my, p7mx, p7my )

desenhaLinha(p4mx, p4my, p8mx, p8my )

desenhaLinha(p5mx, p5my, p6mx, p6my )
desenhaLinha(p5mx, p5my, p7mx, p7my )

desenhaLinha(p6mx, p6my, p8mx, p8my )

desenhaLinha(p7mx, p7my, p8mx, p8my )

plt.show()

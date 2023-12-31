
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Função para calcular uma curva de Bezier cúbica
def bezier_curve(P0, P1, P2, P3, t):
    return (
        (1 - t)**3 * P0 +
        3 * (1 - t)**2 * t * P1 +
        3 * (1 - t) * t**2 * P2 +
        t**3 * P3
    )

# Função para calcular uma curva de Hermite cúbica
def hermite_curve(P0, P1, T0, T1, t):
    t2 = t * t
    t3 = t2 * t
    h00 = (2 * t3 - 3 * t2 + 1)
    h01 = (t3 - 2 * t2 + t)
    h10 = (-2 * t3 + 3 * t2)
    h11 = (t3 - t2)
    return (
        h00 * P0 +
        h10 * P1 +
        h01 * T0 +
        h11 * T1
    )

# Número de pontos ao longo das curvas
num_points = 100

# Inicializar a figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Número de curvas de Bezier, Hermite e retas desejadas
num_curves = 3
num_straights = 2

# Lista para armazenar os pontos de início e fim das curvas
curve_endpoints = []

# Iniciar o ponto de partida
current_point = np.array([0, 0, 0])

for i in range(num_curves):
    # Manter as curvas Bezier e Hermite fixas
    bezier_P0 = current_point
    bezier_P3 = current_point + np.random.rand(3) * 5
    hermite_P0 = current_point
    hermite_P1 = current_point + np.random.rand(3) * 5

    # Gerar pontos de controle aleatórios para a curva Bezier atual
    np.random.seed(i)
    bezier_P1 = np.random.rand(3) * 5
    bezier_P2 = np.random.rand(3) * 5

    # Gerar pontos de controle aleatórios para a curva Hermite atual
    hermite_T0 = np.random.rand(3) * 5
    hermite_T1 = np.random.rand(3) * 5

    # Gerar pontos ao longo das curvas Bezier e Hermite atuais
    bezier_points = np.array([
        bezier_curve(bezier_P0, bezier_P1, bezier_P2, bezier_P3, t)
        for t in np.linspace(0, 1, num_points)
    ])

    hermite_points = np.array([
        hermite_curve(hermite_P0, hermite_P1, hermite_T0, hermite_T1, t)
        for t in np.linspace(0, 1, num_points)
    ])

    # Salvar os pontos de início e fim das curvas
    curve_endpoints.extend([bezier_P0, bezier_P3, hermite_P0, hermite_P1])

    # Plotar as curvas Bezier e Hermite atuais
    ax.plot(bezier_points[:, 0], bezier_points[:, 1], bezier_points[:, 2], label=f'Curva Bezier {i + 1}', color='blue')
    ax.plot(hermite_points[:, 0], hermite_points[:, 1], hermite_points[:, 2], label=f'Curva Hermite {i + 1}', color='red')

    # Atualizar o ponto de partida
    current_point = bezier_P3

# Adicionar retas aleatórias interligadas
for i in range(num_straights):
    start = current_point
    end = current_point + np.random.rand(3) * 5
    ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], color='green')

    # Salvar os pontos de início e fim das retas
    curve_endpoints.extend([start, end])

    # Atualizar o ponto de partida
    current_point = end

# Adicionar a linha de conexão
curve_endpoints = np.array(curve_endpoints)
ax.plot(curve_endpoints[:, 0], curve_endpoints[:, 1], curve_endpoints[:, 2], color='orange')

# Configurações adicionais
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')
ax.legend()

# Mostrar o gráfico
plt.show()

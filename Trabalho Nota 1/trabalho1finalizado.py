import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Adicionando suporte para gráficos 3D

# Define the window and viewport limits
window_limits = {
    'xmin': -1,
    'ymin': -1,
    'xmax': 1,
    'ymax': 1
}

viewport_limits = {
    'xmin': 0,
    'ymin': 0,
    'xmax': 500,
    'ymax': 500
}

# Inicializa matrizes de transformação
transformation_matrices = {
    'translation': np.eye(4),  # Matriz de translação inicializada como matriz de identidade
    'rotation_x': np.eye(4),   # Matriz de rotação em torno do eixo X
    'rotation_y': np.eye(4),   # Matriz de rotação em torno do eixo Y
    'rotation_z': np.eye(4),   # Matriz de rotação em torno do eixo Z
    'scale': np.eye(4)         # Matriz de escala
}

# Inicializa matrizes de transformação da câmera
camera_matrices = {
    'translation': np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, -10], [0, 0, 0, 1]]),
    'rotation_x': np.eye(4),
    'rotation_y': np.eye(4),
    'rotation_z': np.eye(4)
}

# Inicializa matriz de projeção para projeção perspectiva
fovy = math.radians(67.0)
aspect = 1.0
zNear = 0.1
zFar = 100

a = 1 / (math.tan(fovy / 2) * aspect)
b = 1 / (math.tan(fovy / 2))
c = (zFar + zNear) / (zNear - zFar)
d = (2 * zFar * zNear) / (zNear - zFar)

projection_matrix = np.array([
    [a, 0, 0, 0],
    [0, b, 0, 0],
    [0, 0, c, d],
    [0, 0, -1, 0]
])

# Define coordenadas do modelo
model_coordinates = [
    [0.000000, -1.000000, -1.000000, 1.0],
    [0.195090, -1.000000, -0.980785, 1.0],
    # ... Adicione o restante das coordenadas aqui
    [0.000000, 1.000000, 0.000000, 1.0]
]

# Define uma função para realizar o mapeamento
def map_coordinates(p):
    # Configura os limites da área de visualização no gráfico
    plt.xlim(viewport_limits['xmin'], viewport_limits['xmax'])
    plt.ylim(viewport_limits['ymin'], viewport_limits['ymax'])

    # Realiza o mapeamento das coordenadas do modelo para as coordenadas da área de visualização
    xvp = ((p[0] - window_limits['xmin']) * (viewport_limits['xmax'] - viewport_limits['xmin'])) / (window_limits['xmax'] - window_limits['xmin']) + viewport_limits['xmin']
    yvp = ((p[1] - window_limits['ymin']) * (viewport_limits['ymax'] - viewport_limits['ymin'])) / (window_limits['ymax'] - window_limits['ymin']) + viewport_limits['ymin']

    # Plota o ponto mapeado
    plt.scatter(xvp, yvp)

# Define uma função para exibir coordenadas
def display_points(points):
    for point in points:
        print(point)

# Define a função para exibir pontos em 3D
def display_points_3d(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')  # Cria um eixo 3D

    for point in points:
        ax.scatter(point[0], point[1], point[2])  # Plota o ponto em 3D

    # Define rótulos dos eixos
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Mostra o gráfico 3D
    plt.show()

# Menu de opções para interação do usuário
print('\nAplicação que implementa um pipeline de visualização 3D completo\n')

while True:
    print("1. Manipular o objeto")
    print("2. Manipular a Câmera")
    print("3. Modificar projeção")
    print("4. Modificar mapeamento:")
    print("5. Visualizar objeto:")
    print("6. Calculos:")
    print("9. Sair e vizualizar:")

    option = int(input("Digite a opção: "))

    if option == 1:
        print("1. Translação")
        print("2. Escala")
        print("3. Rotação em X")
        print("4. Rotação em Y:")
        print("5. Rotação em Z:")

        operation = int(input("Digite a opção: "))

        if operation == 1:
            tx = float(input("Digite o valor de tx: "))
            ty = float(input("Digite o valor de ty: "))
            tz = float(input("Digite o valor de tz: "))

            # Atualiza a matriz de transformação de translação
            transformation_matrices['translation'] = np.array([
                [1, 0, 0, tx],
                [0, 1, 0, ty],
                [0, 0, 1, tz],
                [0, 0, 0, 1]
            ])
        # ... Adicione o tratamento para outras transformações (escala, rotação)

# Função para exibir o objeto 3D após todas as transformações e projeções
def display_points_3d(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for coord in points:
        ax.scatter(coord[0], coord[1], coord[2], c='r', marker='o')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# Visualiza o objeto 3D após todas as transformações e projeções
display_points_3d(projected_points)

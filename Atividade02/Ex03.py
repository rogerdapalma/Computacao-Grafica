
import numpy as np

# Função para aplicar a transformação escolhida na matriz de transformações (matT)
def apply_transformation(matT, transformation_type, params):
    if transformation_type == "translacao":
        tx, ty = params
        translation_matrix = np.array([[1, 0, tx],
                                       [0, 1, ty],
                                       [0, 0, 1]])
        matT[:] = np.dot(matT, translation_matrix)
    elif transformation_type == "rotacao":
        angle = params
        theta = np.radians(angle)
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],
                                    [np.sin(theta), np.cos(theta), 0],
                                    [0, 0, 1]])
        matT[:] = np.dot(matT, rotation_matrix)
    elif transformation_type == "escala":
        sx, sy = params
        scale_matrix = np.array([[sx, 0, 0],
                                 [0, sy, 0],
                                 [0, 0, 1]])
        matT[:] = np.dot(matT, scale_matrix)

# Função para mostrar a matriz de transformações na tela
def print_matrix(mat):
    print("Matriz de Transformações (matT):")
    print(mat)

# Função para aplicar a transformação matT sobre um ponto (x, y)
def apply_transformation_to_point(matT, point):
    homogenous_point = np.array([point[0], point[1], 1])
    transformed_point = np.dot(matT, homogenous_point)
    return transformed_point[:2]

# Inicialização da matriz de transformações como matriz identidade
matT = np.identity(3)

# Loop para a interação com o usuário
while True:
    print("\nEscolha a transformação:")
    print("1. Translação")
    print("2. Rotação")
    print("3. Escala")
    print("4. Proxima etapa")
    print("5. Sair")

    choice = int(input("Digite o número da opção desejada: "))

    if choice == 1:
        tx = float(input("Digite o valor de tx (translação no eixo x): "))
        ty = float(input("Digite o valor de ty (translação no eixo y): "))
        apply_transformation(matT, "translacao", [tx, ty])
    elif choice == 2:
        angle = float(input("Digite o ângulo de rotação (em graus): "))
        apply_transformation(matT, "rotacao", angle)
    elif choice == 3:
        sx = float(input("Digite o fator de escala em x: "))
        sy = float(input("Digite o fator de escala em y: "))
        apply_transformation(matT, "escala", [sx, sy])
    elif choice == 4:
        x = float(input("Digite o valor de x do ponto: "))
        y = float(input("Digite o valor de y do ponto: "))
        transformed_point = apply_transformation_to_point(matT, [x, y])
        print("Ponto transformado:", transformed_point)
    elif choice == 5:
        print("Encerrando a aplicação.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

    # Mostra a matriz de transformações atualizada
    print_matrix(matT)

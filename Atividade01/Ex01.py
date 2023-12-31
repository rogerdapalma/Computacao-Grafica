import numpy as np

# Função para ler os valores da matriz 3x3 do usuário
def read_matrix():
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            value = float(input(f"Digite o valor da posição [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)
    return np.array(matrix)

# Função para imprimir a matriz na tela
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(elem) for elem in row))

# Função para mostrar o menu de opções e retornar a escolha do usuário
def menu():
    print("1 - Adição e subtração de outra matriz")
    print("2 - Multiplicação e Divisão por um escalar")
    print("3 - Multiplicação por um vetor de 3 elementos")
    print("4 - Multiplicação por outra matriz 3x3")
    print("5 - Apresentar a transposta da matriz inicial")
    print("0 - Sair")
    return int(input("Escolha uma opção: "))

# Função principal do programa
def main():
    print("Preencha a matriz 3x3:")
    matrix = read_matrix()
    
    while True:
        option = menu()
        if option == 1:
            print("\nPreencha a outra matriz 3x3:")
            other_matrix = read_matrix()
            result_add = matrix + other_matrix
            result_sub = matrix - other_matrix
            
            print("\nResultado da adição:")
            print_matrix(result_add)
            
            print("\nResultado da subtração:")
            print_matrix(result_sub)
        elif option == 2:
            scalar = float(input("Digite o valor do escalar: "))
            result_mul = matrix * scalar
            result_div = matrix / scalar
            
            print("\nResultado da multiplicação por escalar:")
            print_matrix(result_mul)
            
            print("\nResultado da divisão por escalar:")
            print_matrix(result_div)
        elif option == 3:
            vector = []
            for i in range(3):
                value = float(input(f"Digite o valor do vetor na posição {i}: "))
                vector.append(value)
            vector = np.array(vector)
            result_mul_vector = np.dot(matrix, vector)
            
            print("\nResultado da multiplicação por vetor:")
            print(result_mul_vector)
        elif option == 4:
            print("\nPreencha a outra matriz 3x3:")
            other_matrix = read_matrix()
            result_mul_matrix = np.dot(matrix, other_matrix)
            
            print("\nResultado da multiplicação por outra matriz:")
            print_matrix(result_mul_matrix)
        elif option == 5:
            transposed_matrix = np.transpose(matrix)
            print("\nTransposta da matriz:")
            print_matrix(transposed_matrix)
        elif option == 0:
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

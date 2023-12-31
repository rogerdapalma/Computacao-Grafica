import numpy as np

# Função para ler os valores x, y e z do vetor de 3 dimensões
def read_vector():
    x = float(input("Digite o valor de x: "))
    y = float(input("Digite o valor de y: "))
    z = float(input("Digite o valor de z: "))
    return np.array([x, y, z])

# Função para imprimir o vetor na tela
def print_vector(vector):
    print("Vetor: [", ", ".join(str(elem) for elem in vector), "]")

# Função para mostrar o menu de opções e retornar a escolha do usuário
def menu():
    print("1 - Calcular o tamanho do vetor")
    print("2 - Normalizar o vetor")
    print("3 - Adicionar outro vetor")
    print("4 - Subtrair outro vetor")
    print("5 - Multiplicação por um escalar")
    print("6 - Divisão por um escalar")
    print("7 - Calcular o produto escalar")
    print("0 - Sair")
    return int(input("Escolha uma opção: "))

# Função principal do programa
def main():
    print("Preencha o vetor de 3 dimensões:")
    vector = read_vector()
    
    while True:
        option = menu()
        if option == 1:
            magnitude = np.linalg.norm(vector)
            print(f"\nTamanho do vetor: {magnitude}")
        elif option == 2:
            normalized_vector = vector / np.linalg.norm(vector)
            print("\nVetor normalizado:")
            print_vector(normalized_vector)
        elif option == 3:
            print("\nPreencha o novo vetor de 3 dimensões:")
            other_vector = read_vector()
            result_add = vector + other_vector
            print("\nResultado da adição:")
            print_vector(result_add)
        elif option == 4:
            print("\nPreencha o novo vetor de 3 dimensões:")
            other_vector = read_vector()
            result_sub = vector - other_vector
            print("\nResultado da subtração:")
            print_vector(result_sub)
        elif option == 5:
            scalar = float(input("Digite o valor do escalar: "))
            result_mul = vector * scalar
            print("\nResultado da multiplicação por escalar:")
            print_vector(result_mul)
        elif option == 6:
            scalar = float(input("Digite o valor do escalar: "))
            result_div = vector / scalar
            print("\nResultado da divisão por escalar:")
            print_vector(result_div)
        elif option == 7:
            print("\nPreencha o novo vetor de 3 dimensões:")
            other_vector = read_vector()
            dot_product = np.dot(vector, other_vector)
            print(f"\nProduto escalar dos vetores: {dot_product}")
        elif option == 0:
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

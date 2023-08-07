import math
import numpy

matriz = numpy.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

print(matriz)

while True:
    print("1. Adição e subtração de outra matriz")
    print("2. Multiplicação e Divisão de um escalar")
    print("3. Multiplicação da matriz por um vetor")
    print("4. Multiplicação da matriz por outra matriz")
    print("5. Apresentar a transposta da matriz")

    op = int(input("Digite a opção: "))

    if op == 1:
        matriz2 = numpy.array([[9,8,7],
                               [6,5,4],
                               [3,2,1]])
        matrizSoma = matriz+matriz2 #soma as duas matrizes
        matrizSub = matriz-matriz2 #subtrai uma matriz da ourta
        print("Soma das matrizes:")
        print(matrizSoma)
        print("Subtração das matrizes")
        print(matrizSub)
    
    elif op == 2:
        escalar = float(input("Digite o escalar: "))
        matrizMultEscalar = matriz*escalar
        matrizDivEscalar = matriz/escalar
        print("Multiplicação por escalar:")
        print(matrizMultEscalar)
        print("Divisão por escalar")
        print(matrizDivEscalar)
    
    elif op == 3:
        vetor = numpy.array([1, 2, 3])
        resultado = matriz.dot(vetor) #dot multiplica a matriz pelo vetor (ou outra matriz)
        print("Matriz multiplicada pelo vetor:")
        print(resultado)
    
    elif op == 4:
        matriz2 = numpy.array([[9, 8, 7],
                               [6, 5, 4],
                               [3, 2, 1]])
        resultado = matriz.dot(matriz2) #multiplica uma matriz por outra
        print("Matriz multiplicada por outra matriz:")
        print(resultado)
    
    elif op == 5:
        resultado = numpy.transpose(matriz) #transpose calcula a transposta da matriz
        print("Matriz transposta:")
        print(resultado)
    
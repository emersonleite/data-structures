""" MATRIZES """

import numpy as np

""" Definindo uma matriz """
matriz = np.array([[2, 3, 1], 
                   [4, 5, 7]])

""" Acessando linhas """
print(matriz[0])

print(matriz[1])

""" Acessando elementos """
print(matriz[0][0])
print(matriz[1][2])

""" Interando sobre a matriz """
s = matriz.shape # tamanho da matriz

for i in range(matriz.shape[0]):
    print(matriz[i])
    for j in range(matriz.shape[1]):
        print(matriz[i][j])
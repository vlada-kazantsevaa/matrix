import numpy as np
A = np.array([[4, 2, 2], [2, 5, 1], [2, 1, 6]])
b = np.array([1, 2, 3])

def transponation (matrix):
    trans_matrix = [[0 for j in range(len(matrix))]for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix

def solving_triangular_matrix(matrix, equals, orientation):
    res = []
    
    if orientation == "upper":
        for m in range(len(matrix)):
            res.append(0)
        for i in reversed(range(len(matrix))):
            if i == len(matrix):
                res[len(matrix)] = (equals[len(matrix)] / matrix[len(matrix)][len(matrix)])
            else:
                sum_of_prev = 0
                for n in reversed(range(i, len(matrix))):
                    sum_of_prev += res[n]*matrix[i][n]
                res[i] = ((equals[i] - sum_of_prev) / matrix[i][i])
        return res
    
    if orientation == "lower":
        for i in range(len(matrix)):
            if i == 0:
                res.append(equals[0] / matrix[0][0])
            else:
                sum_of_prev = 0
                for n in range(0,i):
                    sum_of_prev += res[n]*matrix[i][n]
                res.append((equals[i] - sum_of_prev) / matrix[i][i])
        return res

if np.allclose(A, A.T) and np.all(np.linalg.eigvals(A) > 0):
    def cholesky_decomposition(A):
        n = len(A)
        L = np.zeros_like(A)
        for i in range(n):
            for j in range(i+1):
                s = sum(L[i][k] * L[j][k] for k in range(j))
                if i == j:
                    L[i][i] = np.sqrt(A[i][i] - s)
                else:
                    L[i][j] = (A[i][j] - s) / L[j][j]
        return L
    L = cholesky_decomposition(A)
    trans_L = transponation(L)

    y = solving_triangular_matrix(L,b, orientation="lower")
    x = solving_triangular_matrix(trans_L, y, orientation="upper")
    print("Решение системы уравнений:", x)

else:
    print("Матрица системы уравнений не является симметричной и положительно определенной. Метод Холецкого не применим.")

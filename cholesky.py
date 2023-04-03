import numpy as np
A = np.array([[4, 2, 2], [2, 5, 1], [2, 1, 6]])
b = np.array([1, 2, 3])

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
    
    trans_L = [[0 for j in range(len(L))]for i in range(len(L[0]))]
    for i in range(len(L)):
    	for j in range(len(L[0])):
    		trans_L[j][i] = L[i][j]
    
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(trans_L, y)
    print("Решение системы уравнений:", x)
else:
    print("Матрица системы уравнений не является симметричной и положительно определенной. Метод Холецкого не применим.")
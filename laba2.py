import numpy as np

# ВВОДНЫЕ ДАННЫЕ 
epsilon = 1.0E-2  # погрешность решения
matrix = np.matrix([
    [4, 1, 2, 0.5, 2],
    [1, 0.5, 0, 0, 0],
    [2, 0, 3, 0, 0],
    [0.5, 0, 0, 0.625, 0],
    [2, 0, 0, 0, 16]
    ])
f = np.matrix([1, 1, 1, 1, 1]).transpose()
target = np.matrix([0, 0, 0, 0, 0]).transpose()

# НЕВЯЗКА
def min_discrepancies(A, b, x):
    r = A * x - b  # высчитываем направление невязки (вектор)
    # высчитываем коэф. поправки вектора невязки
    t = np.dot((A * r).transpose(), r) / (np.linalg.norm(A * r)**2)
    x = x - float(t) * r  # новое решение СЛАУ
    return (A, b, x)

# ПРОВЕРКА НА ПОЛОЖИТЕЛЬНУЮ ОПРЕДЕЛЁННОСТЬ
def pd(matrix):
    res = np.all(np.linalg.eigvals(matrix) > 0)
    if not res:
        print("Матрица не является положительно определённой")
    return res

# ПРОВЕРКА НА СИММЕТРИЧНОСТЬ  
def sim(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if matrix[i, j] != matrix[j, i]:
                print("Матрица не является симметричной")
                return False
    return True


print('Матрица A:\n', matrix)
print('Правый вектор: ', f.transpose())
print('Начальный вектор приближения', target.transpose(), end='\n\n')
if not pd(matrix) or not sim(matrix): # проверка на применимость метода
    exit()
counter = 0
# print('Шаг', 'Вектор решения на шаге', sep='\t\t')
while np.linalg.norm(matrix*target - f) > epsilon:  # итерационная часть
    # print(counter, target.transpose(), sep='\t\t')
    matrix, f, target = min_discrepancies(matrix, f, target)
    counter += 1

print('\nВектор решения с точностью ', epsilon, ': ', target.transpose())
print('Количество итераций: ', counter)
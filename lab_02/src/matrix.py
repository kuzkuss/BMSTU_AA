import random

def create_random_mtrx(n, m):
    return [[random.randint(-100, 100) for _ in range(m)] for _ in range(n)]

def input_mtrxs():
    print("Введите первую матрицу:")
    mtrx1 = input_matrix()

    print("Введите вторую матрицу:")
    mtrx2 = input_matrix()

    return mtrx1, mtrx2
    
def input_matrix():
    n = int(input("Введите количество строк: "))
    m = int(input("Введите количество столбцов: "))

    if n <= 0 or m <= 0:
        raise ValueError

    matrix = []
    for i in range(n):
        matrix.append([])
        row = list(map(int, input().split()))
        if len(row) != m:
            raise TypeError
        for j in range(m):
            matrix[i].append(row[j])

    return matrix

def print_matrix(matrix):
    print("Результат:")

    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end = " ")
        print()


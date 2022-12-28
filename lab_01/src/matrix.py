def create_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]

    for i in range(n):
        matrix[i][0] = i
    
    for j in range(m):
        matrix[0][j] = j

    return matrix

def create_matrix_cache(n, m):
    return [[-1] * m for _ in range(n)]


def print_matrix(matrix, str1, str2):
    print('\n ', '0', *list(str2), sep = '   ')

    for i in range(len(str1) + 1):
        if i == 0:
            print('0', end = '')
        else:
            print(str1[i - 1], end = '')

        for j in range(len(str2) + 1):
            print('   ' + str(matrix[i][j]), end = '' if j != len(str2) else '\n')


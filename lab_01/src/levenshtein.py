from matrix import *

def matrix_levenshtein(str1, str2):
    n1 = len(str1) + 1
    n2 = len(str2) + 1

    matrix = create_matrix(n1, n2)

    for i in range(1, n1):
        for j in range(1, n2):
            d1 = matrix[i][j - 1] + 1
            d2 = matrix[i - 1][j] + 1
            d3 = matrix[i - 1][j - 1] + (0 if str1[i - 1] == str2[j - 1] else 1)
            matrix[i][j] = min(d1, d2, d3)
    
    print_matrix(matrix, str1, str2)
    
    return matrix[n1 - 1][n2 - 1]


from matrix import *

def matrix_damerau_levenshtein(str1, str2):
    n1 = len(str1) + 1
    n2 = len(str2) + 1

    matrix = create_matrix(n1, n2)

    for i in range(1, n1):
        for j in range(1, n2):
            d1 = matrix[i][j - 1] + 1
            d2 = matrix[i - 1][j] + 1
            d3 = matrix[i - 1][j - 1] + (0 if str1[i - 1] == str2[j - 1] else 1)
            if i > 1 and j > 1 and str1[i - 1] == str2[j - 2] and str2[j - 1] == str1[i - 2]:
                d4 = matrix[i - 2][j - 2] + 1
                matrix[i][j] = min(d1, d2, d3, d4)
            else:
                matrix[i][j] = min(d1, d2, d3)
    
    print_matrix(matrix, str1, str2)
    
    return matrix[n1 - 1][n2 - 1]

def recursive_damerau_levenshtein(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    if n1 == 0 or n2 == 0:
        return max(n1, n2)

    d1 = recursive_damerau_levenshtein(str1[:], str2[:-1]) + 1
    d2 = recursive_damerau_levenshtein(str1[:-1], str2[:]) + 1
    d3 = recursive_damerau_levenshtein(str1[:-1], str2[:-1]) + \
                                            (0 if str1[-1] == str2[-1] else 1)

    if n1 > 1 and n2 > 1 and str1[-1] == str2[-2] and str2[-1] == str1[-2]:
        d4 = recursive_damerau_levenshtein(str1[:-2], str2[:-2]) + 1
        return min(d1, d2, d3, d4)
    else:
        return min(d1, d2, d3)

def rec_dam_lev_mtrx(str1, str2, matrix):
    n1 = len(str1)
    n2 = len(str2)

    if matrix[n1][n2] == -1:
        if n1 == 0 or n2 == 0:
            matrix[n1][n2] = max(n1, n2)

        else:
            d1 = rec_dam_lev_mtrx(str1[:], str2[:-1], matrix) + 1
            d2 = rec_dam_lev_mtrx(str1[:-1], str2[:], matrix) + 1
            d3 = rec_dam_lev_mtrx(str1[:-1], str2[:-1], matrix) + \
                                                    (0 if str1[-1] == str2[-1] else 1)

            if n1 > 1 and n2 > 1 and str1[-1] == str2[-2] and str2[-1] == str1[-2]:
                d4 = rec_dam_lev_mtrx(str1[:-2], str2[:-2], matrix) + 1
                matrix[n1][n2] = min(d1, d2, d3, d4)
            else:
                matrix[n1][n2] = min(d1, d2, d3)

    return matrix[n1][n2]

def recursive_damerau_levenshtein_cache(str1, str2):
    matrix = create_matrix_cache(len(str1) + 1, len(str2) + 1)
    res = rec_dam_lev_mtrx(str1, str2, matrix)
    print_matrix(matrix, str1, str2)
    return res
    

    
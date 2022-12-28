def classic_multiplication(mtrx1, mtrx2):
    n, l, m = len(mtrx1), len(mtrx1[0]), len(mtrx2[0])

    res_mtrx = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(l):
                res_mtrx[i][j] += mtrx1[i][k] * mtrx2[k][j]

    return res_mtrx

def winograd_multiplication(mtrx1, mtrx2):
    n, l, m = len(mtrx1), len(mtrx1[0]), len(mtrx2[0])

    res_mtrx = [[0] * m for _ in range(n)]

    tmp_mtrx1 = precompute_rows(mtrx1, n, l)
    tmp_mtrx2 = precompute_cols(mtrx2, l, m)

    for i in range(n):
        for j in range(m):
            res_mtrx[i][j] = -tmp_mtrx1[i] - tmp_mtrx2[j]
            for k in range(l // 2):
                res_mtrx[i][j] = res_mtrx[i][j] + (mtrx1[i][k * 2] + mtrx2[k * 2 + 1][j]) * \
                                                        (mtrx1[i][k * 2 + 1] + mtrx2[k * 2][j])

    if l % 2 != 0:
        for i in range(n):
            for j in range(m):
                res_mtrx[i][j] = res_mtrx[i][j] + mtrx1[i][l - 1] * mtrx2[l - 1][j]
    return res_mtrx

def precompute_rows(mtrx, n, m):
    res_vec = [0] * n

    for i in range(n):
        for j in range(m // 2):
            res_vec[i] = res_vec[i] + mtrx[i][j * 2] * mtrx[i][j * 2 + 1]
	
    return res_vec

def precompute_cols(mtrx, n, m):
    res_vec = [0] * m

    for i in range(m):
        for j in range(n // 2):
            res_vec[i] = res_vec[i] + mtrx[j * 2][i] * mtrx[j * 2 + 1][i]
	
    return res_vec

def optimized_winograd_multiplication(mtrx1, mtrx2):
    n, l, m = len(mtrx1), len(mtrx1[0]), len(mtrx2[0])

    res_mtrx = [[0] * m for _ in range(n)]

    tmp_mtrx1 = optimized_precompute_rows(mtrx1, n, l)
    tmp_mtrx2 = optimized_precompute_cols(mtrx2, l , m)

    for i in range(n):
        for j in range(m):
            temp = -tmp_mtrx1[i] - tmp_mtrx2[j]
            for k in range(l // 2):
                temp += (mtrx1[i][k << 1] + mtrx2[(k << 1) + 1][j]) * (mtrx1[i][(k << 1) + 1] + mtrx2[k << 1][j])
            res_mtrx[i][j] = temp

    if l % 2 != 0:
        for i in range(n):
            for j in range(m):
                res_mtrx[i][j] += mtrx1[i][l - 1] * mtrx2[l - 1][j]
    return res_mtrx

def optimized_precompute_rows(mtrx, n, m):
    res_vec = [0] * n

    for i in range(n):
        for j in range(m // 2):
            res_vec[i] += mtrx[i][j << 1] * mtrx[i][(j << 1) + 1]
	
    return res_vec

def optimized_precompute_cols(mtrx, n, m):
    res_vec = [0] * m

    for i in range(m):
        for j in range(n // 2):
            res_vec[i] += mtrx[j << 1][i] * mtrx[(j << 1) + 1][i]
	
    return res_vec


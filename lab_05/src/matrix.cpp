// Удаление из матрицы в схеме крм элементов <= q:
// генератор разреженных матриц
// удаление элементов
// лог исходной и измененной матрицы в файл

#include <cstring>
#include <fstream>
#include "matrix.h"

void init_matrix(matrix_t* matrix) {
    matrix->AN = nullptr;
    matrix->NR = nullptr;
    matrix->NC = nullptr;
    matrix->JR = nullptr;
    matrix->JC = nullptr;
    matrix->size = 0;
    matrix->amount = 0;
}

void create_matrix(matrix_t* matrix)
{
    srand(time(0));

    matrix->amount = (1 + matrix->size) * matrix->size / 2;

    matrix->JR = new int[matrix->size];
    matrix->JC = new int[matrix->size];
    matrix->AN = new int[matrix->amount];
    matrix->NR = new int[matrix->amount];
    matrix->NC = new int[matrix->amount];

    int idx = 0;
    for (int i = 0; i < matrix->size; ++i) {
        for (int j = i; j < matrix->size; ++j) {
            int tmp;
            tmp = rand() % MAX_NUM + 1;

            matrix->AN[idx] = tmp;
            if (j < matrix->size - 1) {
                matrix->NR[idx] = idx + 2;
            } else {
                matrix->NR[idx] = idx - j + i + 1;
            }
            if (i < j) {
                matrix->NC[idx] = idx + matrix->size - i;
            } else {
                matrix->NC[idx] = idx - matrix->size * i + (1 + i) * i / 2 + 1;
                matrix->JR[i] = idx + 1;
            }
            
            if (i == 0) {
                matrix->JC[j] = idx + 1;
            }
            ++idx;
        }
    }
}

void free_matrix(matrix_t* matrix)
{
    delete [] matrix->JR;
    delete [] matrix->JC;
    delete [] matrix->AN;
    delete [] matrix->NR;
    delete [] matrix->NC;
}

void delete_element(int *arr, int idx, int n) {
    for (int i = idx; i < n - 1; ++i) {
        arr[i] = arr[i + 1];
    }
}

void delete_elements_from_matrix(matrix_t *matrix, int q) {
    for (int i = 0; i < matrix->amount;) {
        if (matrix->AN[i] <= q) {
            for (int j = 0; j < matrix->amount; ++j) {
                if (matrix->NR[j] == i + 1) {
                    matrix->NR[j] = matrix->NR[i];
                }
                if (matrix->NC[j] == i + 1) {
                    matrix->NC[j] = matrix->NC[i];
                }
            }
            for (int m = 0; m < matrix->size; ++m) {
                if (matrix->JR[m] == i + 1) {
                    if (matrix->NR[i] == i + 1) {
                        matrix->JR[m] = 0;
                    } else {
                        matrix->JR[m] = matrix->NR[i];
                    }
                }
                if (matrix->JR[m] > i + 1) {
                    --matrix->JR[m];
                }
                if (matrix->JC[m] == i + 1) {
                    if (matrix->NC[i] == i + 1) {
                        matrix->JC[m] = 0;
                    } else {
                        matrix->JC[m] = matrix->NC[i];
                    }
                }
                if (matrix->JC[m] > i + 1) {
                    --matrix->JC[m];
                }
            }
            delete_element(matrix->NR, i, matrix->amount);
            delete_element(matrix->AN, i, matrix->amount);
            delete_element(matrix->NC, i, matrix->amount);
            --matrix->amount;
            for (int j = 0; j < matrix->amount; ++j) {
                if (matrix->NC[j] > i + 1) {
                    --matrix->NC[j];
                }
                if (matrix->NR[j] > i + 1) {
                    --matrix->NR[j];
                }
            }
        } else {
            ++i;
        }
    }
}

void print_matrix(matrix_t* matrix, int num)
{
    ofstream fout("matrix" + to_string(num) + ".txt", ios_base::app);
    fout << "AN:";
    for (int i = 0; i < matrix->amount; ++i) {
        fout << matrix->AN[i] << " ";
    }
    fout << endl;

    fout << "NR:";
    for (int i = 0; i < matrix->amount; ++i) {
        fout << matrix->NR[i] << " ";
    }
    fout << endl;

    fout << "NC:";
    for (int i = 0; i < matrix->amount; ++i) {
        fout << matrix->NC[i] << " ";
    }
    fout << endl;

    fout << "JR:";
    for (int i = 0; i < matrix->size; ++i) {
        fout << matrix->JR[i] << " ";
    }
    fout << endl;

    fout << "JC:";
    for (int i = 0; i < matrix->size; ++i) {
        fout << matrix->JC[i] << " ";
    }
    fout << endl;
    fout << endl;
    fout << endl;

    fout.close();
}


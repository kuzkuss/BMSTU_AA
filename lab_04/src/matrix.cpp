#include <cstring>

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

void create_matrix(matrix_t* matrix, int size)
{
    srand(time(NULL));
    matrix->size = size;

    matrix->amount = (1 + matrix->size) * matrix->size / 2;

    matrix->JR = new int[matrix->size];
    matrix->JC = new int[matrix->size];
    matrix->AN = new int[matrix->amount];
    matrix->NR = new int[matrix->amount];
    matrix->NC = new int[matrix->amount];

    int idx = 0;
    for (int i = 0; i < matrix->size; ++i) {
        for (int j = 0; j < matrix->size; ++j) {
            if (i <= j) {
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
                }

                if (i == j) {
                    matrix->JR[i] = idx + 1;
                }
                if (i == 0) {
                    matrix->JC[j] = idx + 1;
                }
                ++idx;
            }
        }
    }

    print_matrix(matrix);
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

void delete_elements_from_matrix(matrix_t *matrix, int k) {
    for (int i = 0; i < matrix->amount;) {
        if (matrix->AN[i] > k) {
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

matrix_t *process (matrix_t matrix, int Q) {
    cout << "RESULT:" << endl;
    matrix_t *results = new matrix_t[Q];
    for (int k = 0; k < Q; ++k) {
        results[k].amount = matrix.amount;
        results[k].size = matrix.size;
        results[k].JR = new int[matrix.size];
        results[k].JC = new int[matrix.size];
        results[k].AN = new int[matrix.amount];
        results[k].NR = new int[matrix.amount];
        results[k].NC = new int[matrix.amount];

        memcpy(results[k].JR, matrix.JR, matrix.size * sizeof(int));
        memcpy(results[k].JC, matrix.JC, matrix.size * sizeof(int));
        memcpy(results[k].AN, matrix.AN, matrix.amount * sizeof(int));
        memcpy(results[k].NR, matrix.NR, matrix.amount * sizeof(int));
        memcpy(results[k].NC, matrix.NC, matrix.amount * sizeof(int));

        delete_elements_from_matrix(&results[k], k + 1);
    }
    return results;
}

void print_matrix(matrix_t* matrix)
{
    cout << "AN:";
    for (int i = 0; i < matrix->amount; ++i) {
        cout << matrix->AN[i] << " ";
    }
    cout << endl;

    cout << "NR:";
    for (int i = 0; i < matrix->amount; ++i) {
        cout << matrix->NR[i] << " ";
    }
    cout << endl;

    cout << "NC:";
    for (int i = 0; i < matrix->amount; ++i) {
        cout << matrix->NC[i] << " ";
    }
    cout << endl;

    cout << "JR:";
    for (int i = 0; i < matrix->size; ++i) {
        cout << matrix->JR[i] << " ";
    }
    cout << endl;

    cout << "JC:";
    for (int i = 0; i < matrix->size; ++i) {
        cout << matrix->JC[i] << " ";
    }
    cout << endl;
}

void parallel_process(matrix_t* matrix, std::vector<matrix_t> results, int count_threads, int thread_index, int Q)
{
    cout << endl << "======== THREAD " << thread_index + 1 << " START" << endl;

    int step = Q / count_threads;
    int start = thread_index * step;

    if (thread_index + 1 == count_threads)
    {
        step += Q - step * count_threads;
    }

    for (int k = start; k < start + step; k++)
    {
        results[k].amount = matrix->amount;
        results[k].size = matrix->size;
        results[k].JR = new int[matrix->size];
        results[k].JC = new int[matrix->size];
        results[k].AN = new int[matrix->amount];
        results[k].NR = new int[matrix->amount];
        results[k].NC = new int[matrix->amount];

        memcpy(results[k].JR, matrix->JR, matrix->size * sizeof(int));
        memcpy(results[k].JC, matrix->JC, matrix->size * sizeof(int));
        memcpy(results[k].AN, matrix->AN, matrix->amount * sizeof(int));
        memcpy(results[k].NR, matrix->NR, matrix->amount * sizeof(int));
        memcpy(results[k].NC, matrix->NC, matrix->amount * sizeof(int));

        delete_elements_from_matrix(&results[k], k + 1);

        cout << "k = " << k + 1 << endl;
        print_matrix(&results[k]);
    }

    cout << endl << "======== THREAD " << thread_index + 1 << " END" << endl;
}

std::vector<matrix_t> multithreading(int count_threads, matrix_t* matrix, int Q)
{
    std::vector<std::thread> threads(count_threads);
    std::vector<matrix_t> results(Q);

    for (int i = 0; i < count_threads; i++)
    {
        threads[i] = std::thread(parallel_process, std::ref(matrix), std::ref(results), count_threads, i, Q);
    }

    for (int i = 0; i < count_threads; i++)
    {
        threads[i].join();
    }

    return results;
}

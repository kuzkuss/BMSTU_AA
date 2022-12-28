#include <iostream>

using namespace std;

#include "matrix.h"
#include "time_test.h"
#include "constants.h"

void single_threaded()
{
    matrix_t matrix;

    init_matrix(&matrix);

    int n;
    cout << "Введите размерность матрицы:" << endl;
    cin >> n;

    create_matrix(&matrix, n);

    int Q;
    cout << "Введите ограничение Q:" << endl;
    cin >> Q;

    matrix_t *result = process(matrix, Q);

    for (int i = 0; i < Q; ++i) {
        cout << "k = " << i + 1 << endl;
        print_matrix(&result[i]);
        free_matrix(&result[i]);
    }

    free_matrix(&matrix);
    delete [] result;
}

void multi_threaded()
{
    matrix_t matrix;

    init_matrix(&matrix);

    int n;
    cout << "Введите размерность матрицы:" << endl;
    cin >> n;
    
    create_matrix(&matrix, n);

    int Q;
    cout << "Введите ограничение Q:" << endl;
    cin >> Q;

    cout << endl << "Введите число потоков:" << endl;
    int count_threads;
    cin >> count_threads;

    if (count_threads < 1)
    {
        cout << endl << "Неверное число потоков." << endl;
        free_matrix(&matrix);
        return;
    }

    std::vector<matrix_t> result = multithreading(count_threads, &matrix, Q);

    for (int i = 0; i < Q; ++i) {
        free_matrix(&result[i]);
    }

    free_matrix(&matrix);
}

int main(void)
{
    bool process = true;
    int command;
    int measure_type;
    int count_threads = 1;

    while (process)
    {
        cout << endl << MSG;
        cin >> command;

        if (command == SINGLE)
        {
            single_threaded();
        }
        else if (command == MULTI)
        {
            multi_threaded();
        }
        else if (command == TIME_TEST)
        {
            int size;
            cout << endl << "Введите размер матрицы: ";
            cin >> size;

            measure_time(size);
        }
        else
        {
            process = false;
        }
    }

    return OK;
}
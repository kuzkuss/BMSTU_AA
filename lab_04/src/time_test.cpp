#include "time_test.h"

void measure_time(int size)
{
    std::chrono::time_point<std::chrono::system_clock> start, end;
    double result_single = 0;
    double result_multi = 0;

    matrix_t matrix;
    init_matrix(&matrix);

    for (int i = 1; i < 33; i++)
    {
        for (int j = 0; j < ITERS; j++)
        {
            create_matrix(&matrix, size);

            start = std::chrono::system_clock::now();
            matrix_t *results = process(matrix, 500);
            end = std::chrono::system_clock::now();

            result_single += (std::chrono::duration_cast<std::chrono::nanoseconds> 
            (end - start).count());
            free(results);

            start = std::chrono::system_clock::now();
            multithreading(i, &matrix, 500);
            end = std::chrono::system_clock::now();

            result_multi += (std::chrono::duration_cast<std::chrono::nanoseconds> 
            (end - start).count());

            cout << endl << j << " iter";
            free_matrix(&matrix);
        }
        
        result_single /= ITERS;
        result_multi /= ITERS;

        write_in_file(size, 1, result_single, FILE_SINGLE);
        write_in_file(size, i, result_multi, FILE_MULTI);
    }    
}

void write_in_file(int size, int count_threads, double time_result, int choice)
{
    if (choice == FILE_MULTI) 
    {
        ofstream fout(NAME_MULTI, ios_base::app);
        fout << to_string(count_threads);
        fout << " " << to_string(time_result) << "\n";
        fout.close();
    }
    else if (choice == FILE_SINGLE)
    {
        ofstream fout(NAME_SINGLE, ios_base::app);
        fout << to_string(count_threads);
        fout << " " << to_string(time_result) << "\n";
        fout.close();
    }
}


#include "time_test.h"

void write_in_file(int size, int count, double time_result, int choice)
{
    if (choice == LINEAR) 
    {
        ofstream fout(NAME_SINGLE, ios_base::app);
        fout << to_string(count);
        fout << " " << to_string(time_result) << "\n";
        fout.close();
    }
    else if (choice == PARALLEL)
    {
        ofstream fout(NAME_MULTI, ios_base::app);
        fout << to_string(count);
        fout << " " << to_string(time_result) << "\n";
        fout.close();
    }
}

void test_n()
{
    int process_type;
    std::chrono::time_point<std::chrono::system_clock> start, end;
    double result_single = 0;
    double result_multi = 0;

    int size;

    std::cout << "\nРазмерность матриц : ";
    std::cin >> size;
    for ( int count = 10; count < 60; count += 10 )
    {
        for (int j = 0; j < ITERS; j++)
        {
            start = std::chrono::system_clock::now();
            linear_mode(size, count);
            end = std::chrono::system_clock::now();

            result_single += (std::chrono::duration_cast<std::chrono::nanoseconds> 
            (end - start).count());

            start = std::chrono::system_clock::now();
            parallel_mode(size, count);
            end = std::chrono::system_clock::now();

            result_multi += (std::chrono::duration_cast<std::chrono::nanoseconds> 
            (end - start).count());

            cout << endl << j << " iter";
        }
        
        result_single /= ITERS;
        result_multi /= ITERS;

        write_in_file(size, count, result_single, LINEAR);
        write_in_file(size, count, result_multi, PARALLEL);
    }
}


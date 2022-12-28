#include "conveyor.h"
#include "constants.h"

double cur_time;

std::vector<double> cur_time1;
std::vector<double> cur_time2;
std::vector<double> cur_time3;

void linear_log(matrix_t *mtrx, const int belt, const int task)
{
    std::chrono::time_point<std::chrono::system_clock> start, end;
    double result = 0;

    if ( belt == FIRST )
    {
        start = std::chrono::system_clock::now();
        create_matrix(mtrx);
        end = std::chrono::system_clock::now();
        print_matrix(mtrx, task);
    }
    else if ( belt == SECOND )
    {
        start = std::chrono::system_clock::now();
        delete_elements_from_matrix(mtrx, 5);
        end = std::chrono::system_clock::now();
    }
    else if ( belt == THIRD )
    {
        start = std::chrono::system_clock::now();
        print_matrix(mtrx, task);
        end = std::chrono::system_clock::now();
        free_matrix(mtrx);
    }

    result = (std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count()) / IN_SEC;
    printf("Tape: %d  Task: %d  Start Time: %.6f  End Time: %.6f\n", belt, task, cur_time, cur_time + result);
    cur_time += result;
}


void linear_mode(int size, int n)
{
    std::queue<matrix_t> q1;
    std::queue<matrix_t> q2;
    std::queue<matrix_t> q3;

    for ( int i = 0; i < n; ++i )
    {
        matrix_t mtrx;
        init_matrix(&mtrx);

        mtrx.size = size;

        q1.push(mtrx);
    }

    for ( int i = 0; i < n; ++i )
    {
        matrix_t mtrx = q1.front();
        linear_log(&mtrx, 1, i + 1);
        q2.push(mtrx);
        q1.pop();

        mtrx = q2.front();
        linear_log(&mtrx, 2, i + 1);
        q3.push(mtrx);
        q2.pop();

        mtrx = q3.front();
        linear_log(&mtrx, 3, i + 1);
        q3.pop();
    }
}


void parallel_log(matrix_t *mtrx, const int belt, const int task)
{
    std::chrono::time_point<std::chrono::system_clock> start, end;
    double result = 0, start_time;

    if ( belt == FIRST )
    {
        start = std::chrono::system_clock::now();
        create_matrix(mtrx);
        end = std::chrono::system_clock::now();
        result = (std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count()) / IN_SEC;

        start_time = cur_time1[task - 1];
        cur_time1[task] = start_time + result;
        cur_time2[task - 1] = cur_time1[task];
        print_matrix(mtrx, task);
    }
    else if ( belt == SECOND )
    {
        start = std::chrono::system_clock::now();
        delete_elements_from_matrix(mtrx, 5);
        end = std::chrono::system_clock::now();
        result = (std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count()) / IN_SEC;

        start_time = cur_time2[task - 1];
        cur_time2[task] = start_time + result;
        cur_time3[task - 1] = cur_time2[task];
    }
    else if ( belt == THIRD )
    {
        start = std::chrono::system_clock::now();
        print_matrix(mtrx, task);
        end = std::chrono::system_clock::now();
        result = (std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count()) / IN_SEC;

        start_time = cur_time3[task - 1];
        cur_time3[task] = start_time + result;
        free_matrix(mtrx);
    }
}

void first_belt(std::queue<matrix_t>& q1, std::queue<matrix_t>& q2)
{
    int task = 0;
    std::mutex m;

    while ( !q1.empty())
    {
        m.lock();
        matrix_t mtrx = q1.front();
        m.unlock();

        parallel_log(&mtrx, 1, ++task);

        m.lock();
        q2.push(mtrx);
        q1.pop();
        m.unlock();
    }
}


void second_belt(std::queue<matrix_t>& q1, std::queue<matrix_t>& q2, std::queue<matrix_t>& q3)
{
    int task = 0;
    std::mutex m;

    do
    {
        if ( !q2.empty() )
        {
            m.lock();
            matrix_t mtrx = q2.front();
            m.unlock();

            parallel_log(&mtrx, 2, ++task);

            m.lock();
            q3.push(mtrx);
            q2.pop();
            m.unlock();
        }
    } while ( !q1.empty() || !q2.empty() );
}


void third_belt(std::queue<matrix_t>& q1, std::queue<matrix_t>& q2, std::queue<matrix_t>& q3)
{
    int task = 0;
    std::mutex m;

    do
    {
        if ( !q3.empty() )
        {
            m.lock();
            matrix_t mtrx = q3.front();
            m.unlock();

            parallel_log(&mtrx, 3, ++task);

            m.lock();
            q3.pop();
            m.unlock();
        }
    } while ( !q1.empty() || !q2.empty() || !q3.empty() );
}


void parallel_mode(int size, int n)
{
    std::queue<matrix_t> q1;
    std::queue<matrix_t> q2;
    std::queue<matrix_t> q3;

    for ( int i = 0; i < n; ++i )
    {
        matrix_t mtrx;
        init_matrix(&mtrx);

        mtrx.size = size;

        q1.push(mtrx);
    }
    
    for ( int i = 0; i < n + 1; ++i )
    {
        cur_time1.push_back(0);
        cur_time2.push_back(0);
        cur_time3.push_back(0);
    }

    std::vector<std::thread> threads(COUNT_THREADS);

    threads[0] = std::thread(first_belt, std::ref(q1), std::ref(q2));
    threads[1] = std::thread(second_belt, std::ref(q1), std::ref(q2), std::ref(q3));
    threads[2] = std::thread(third_belt, std::ref(q1), std::ref(q2), std::ref(q3));

    for ( int i = 0; i < COUNT_THREADS; ++i )
    {
        threads[i].join();
    }

    cout << endl;
    for ( int i = 0; i < n; ++i )
    {
        printf("Tape: 1  Task: %d  Start Time: %.6f  End Time: %.6f\n", i + 1, cur_time1[i], cur_time1[i + 1]);
    }
    for ( int i = 0; i < n; ++i )
    {
        printf("Tape: 2  Task: %d  Start Time: %.6f  End Time: %.6f\n", i + 1, cur_time2[i], cur_time2[i + 1]);
    }
    for ( int i = 0; i < n; ++i )
    {
        printf("Tape: 3  Task: %d  Start Time: %.6f  End Time: %.6f\n", i + 1, cur_time3[i], cur_time3[i + 1]);
    }
}
 
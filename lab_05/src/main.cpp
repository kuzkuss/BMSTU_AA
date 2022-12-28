#include <iostream>

using namespace std;

#include "matrix.h"
#include "time_test.h"
#include "constants.h"
#include "conveyor.h"

int main(void)
{
    setbuf(stdout, NULL);
    bool process = true;
    int command;

    while (process)
    {
        cout << endl << MSG;
        cin >> command;

        if ( command == LINEAR )
        {
            int size;
            cout << "Введите размерность матриц:" << endl;
            cin >> size;

            int n;
            cout << "Введите количество матриц:" << endl;
            cin >> n;

            linear_mode(size, n);
        }
        else if ( command == PARALLEL )
        {
            int size;
            cout << "Введите размерность матриц:" << endl;
            cin >> size;

            int n;
            cout << "Введите количество матриц:" << endl;
            cin >> n;

            parallel_mode(size, n);
        }
        else if ( command == TIME_N )
        {
            test_n();
        }
        else if ( command == FINISH )
        {
            process = false;
        }
        else
        {
            cout << endl << "Неверный пункт меню";
        }
    }
    return OK;
}




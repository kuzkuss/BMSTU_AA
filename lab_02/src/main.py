from matrix import *
from measurements import *

EXIT = 0
CLASSIC = 1
WINOGRAD = 2
OPTIMIZED_WINOGRAD = 3
MEASUREMENTS = 4

INVALID_CHOICE_MSG = "Неверный выбор!"
INVALID_INPUT_MSG = "Неверный ввод! Размерность и элементы матрицы должны быть целыми числами!"
INVALID_MATRIX_MSG = "Неверный ввод! Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы!"
INVALID_INPUT_ROW_MSG = "Неверный ввод! Количество столбцов матрицы отлично от количества введенных элементов в строке!"

MENU_INFO = \
'''
МЕНЮ:
1 - Классический алгоритм умножения матриц
2 - Умножение матриц по алгоритму Винограда
3 - Умножение матриц по алгоритму Винограда с оптимизациями
4 - Замеры времени
0 - Выход
Выбор:
'''

def print_error(error_msg):
    print(error_msg)

def run():
    choice = 1
    while choice != EXIT:
        choice = int(input(MENU_INFO))
        if choice == CLASSIC:
            try:
                mtrx1, mtrx2 = input_mtrxs()
            except ValueError:
                print_error(INVALID_INPUT_MSG)
                return
            except TypeError:
                print_error(INVALID_INPUT_ROW_MSG)
                return
            if len(mtrx1[0]) != len(mtrx2):
                print_error(INVALID_MATRIX_MSG)
                return
            res_mtrx = classic_multiplication(mtrx1, mtrx2)
            print_matrix(res_mtrx)
        elif choice == WINOGRAD:
            try:
                mtrx1, mtrx2 = input_mtrxs()
            except ValueError:
                print_error(INVALID_INPUT_MSG)
                return
            except TypeError:
                print_error(INVALID_INPUT_ROW_MSG)
                return
            if len(mtrx1[0]) != len(mtrx2):
                print_error(INVALID_MATRIX_MSG)
                return
            res_mtrx = winograd_multiplication(mtrx1, mtrx2)
            print_matrix(res_mtrx)
        elif choice == OPTIMIZED_WINOGRAD:
            try:
                mtrx1, mtrx2 = input_mtrxs()
            except ValueError:
                print_error(INVALID_INPUT_MSG)
                return
            except TypeError:
                print_error(INVALID_INPUT_ROW_MSG)
                return
            if len(mtrx1[0]) != len(mtrx2):
                print_error(INVALID_MATRIX_MSG)
                return
            res_mtrx = optimized_winograd_multiplication(mtrx1, mtrx2)
            print_matrix(res_mtrx)
        elif choice == MEASUREMENTS:
            time_measurements()
        elif choice != EXIT:
            print_error(INVALID_CHOICE_MSG)
            return
            

if __name__ == "__main__":
    run()


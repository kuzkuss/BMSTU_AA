from array import input_array, print_array
from measurements import *

EXIT = 0
BEAD_SORT = 1
COUNTING_SORT = 2
GNOME_SORT = 3
MEASUREMENTS = 4

INVALID_CHOICE_MSG = "Неверный выбор!"
INVALID_INPUT_MSG = "Неверный ввод! Размер и элементы массива должны быть целыми числами!"

MENU_INFO = \
'''
МЕНЮ:
1 - Сортировка бусинами
2 - Сортировка подсчетом
3 - Гномья сортировка
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
        if choice == BEAD_SORT:
            try:
                arr = input_array()
            except ValueError:
                print_error(INVALID_INPUT_MSG)
                return
            bead_sort(arr)
            print_array(arr)
        elif choice == COUNTING_SORT:
            try:
                arr = input_array()
            except ValueError:
                print_error(INVALID_INPUT_MSG)
                return
            counting_sort(arr)
            print_array(arr)
        elif choice == GNOME_SORT:
            try:
                arr = input_array()
            except ValueError:
                print_error(INVALID_INPUT_MSG)
                return
            gnome_sort(arr)
            print_array(arr)
        elif choice == MEASUREMENTS:
            time_measurements()
        elif choice != EXIT:
            print_error(INVALID_CHOICE_MSG)
            

if __name__ == "__main__":
    run()


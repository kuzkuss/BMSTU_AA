from levenshtein import *
from damerau_levenshtein import *
from measurements import *

EXIT = 0
MATRIX_LEVENSHTEIN = 1
MATRIX_DAMERAU_LEVENSHTEIN = 2
RECURSIVE_DAMERAU_LEVENSHTEIN = 3
RECURSIVE_DAMERAU_LEVENSHTEIN_CACHE = 4
MEASUREMENTS = 5

MENU_INFO = \
'''
МЕНЮ:
1 - Вычисление расстояния Левенштейна при помощи нерекурсивного алгоритма
2 - Вычисление расстояния Дамерау-Левенштейна при помощи нерекурсивного алгоритма
3 - Вычисление расстояния Дамерау-Левенштейна при помощи рекурсивного алгоритма
4 - Вычисление расстояния Дамерау-Левенштейна при помощи рекурсивного алгоритма с кешем
5 - Замеры времени
0 - Выход
Выбор:
'''

def input_strs():
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")

    return str1, str2

def print_distance(res):
    print("Полученное расстояние:", res)

def print_error():
    "Неверный выбор!"

def run():
    choice = 1
    while choice != EXIT:
        choice = int(input(MENU_INFO))
        if choice == MATRIX_LEVENSHTEIN:
            str1, str2 = input_strs()
            print_distance(matrix_levenshtein(str1, str2))
        elif choice == MATRIX_DAMERAU_LEVENSHTEIN:
            str1, str2 = input_strs()
            print_distance(matrix_damerau_levenshtein(str1, str2))
        elif choice == RECURSIVE_DAMERAU_LEVENSHTEIN:
            str1, str2 = input_strs()
            print_distance(recursive_damerau_levenshtein(str1, str2))
        elif choice == RECURSIVE_DAMERAU_LEVENSHTEIN:
            str1, str2 = input_strs()
            print_distance(recursive_damerau_levenshtein(str1, str2))
        elif choice == RECURSIVE_DAMERAU_LEVENSHTEIN_CACHE:
            str1, str2 = input_strs()
            print_distance(recursive_damerau_levenshtein_cache(str1, str2))
        elif choice == MEASUREMENTS:
            time_measurements()
        elif choice != EXIT:
            print_error()
            

if __name__ == "__main__":
    run()

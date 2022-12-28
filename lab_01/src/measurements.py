import string
import random
import time
import matplotlib.pyplot as plt

from damerau_levenshtein import *
from levenshtein import *

REPEATS = 100
LENS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_time(str1, str2, alg):
    avgTime = 0

    for _ in range(REPEATS):
        start = time.process_time_ns()
        alg(str1, str2)
        avgTime += time.process_time_ns() - start

    avgTime = avgTime / REPEATS

    return avgTime

def get_random_string(len):
    return ''.join((random.choice(string.ascii_lowercase)) for _ in range(len))


def get_times(algs, LENS):
    times = [[] for _ in range(len(algs))]

    for len in LENS:
        print("Подсчёт для длины ", len)
        str1 = get_random_string(len)
        str2 = get_random_string(len)

        for i, alg in enumerate(algs):
            algTime = (get_time(str1, str2, alg))
            times[i].append(algTime)

    return times

def time_measurements():
    algs = [recursive_damerau_levenshtein, recursive_damerau_levenshtein_cache]
    times_dam_lev_rec_vs_cache = get_times(algs, LENS)

    plt.figure(figsize=(7, 9))
    labels = ['Рекурсивный', 'Рекурсивный с кешем']
    for i, times in enumerate(times_dam_lev_rec_vs_cache):
        plt.plot(LENS, times, label=labels[i])

    plt.title("График зависимости затрат времени от длины слов для алгоритмов\nпоиска расстояния Дамерау-Левенштейна\n")
    plt.xlabel("Длина строк", fontsize=14)
    plt.ylabel("Время, ns", fontsize=14)
    plt.grid(True)
    plt.legend()

    algs = [matrix_damerau_levenshtein, recursive_damerau_levenshtein]
    times_dam_lev_rec_vs_matrix = get_times(algs, LENS)

    plt.figure(figsize=(7, 9))
    labels = ['Матричный', 'Рекурсивный']
    for i, times in enumerate(times_dam_lev_rec_vs_matrix):
        plt.plot(LENS, times, label=labels[i])

    plt.title("График зависимости затрат времени от длины слов для алгоритмов\nпоиска расстояния Дамерау-Левенштейна\n")
    plt.xlabel("Длина строк", fontsize=14)
    plt.ylabel("Время, ns", fontsize=14)
    plt.grid(True)
    plt.legend()

    algs = [matrix_damerau_levenshtein, recursive_damerau_levenshtein_cache]
    times_dam_lev_cache_vs_matrix = get_times(algs, LENS)

    plt.figure(figsize=(7, 9))
    labels = ['Матричный', 'Рекурсивный с кешем']
    for i, times in enumerate(times_dam_lev_cache_vs_matrix):
        plt.plot(LENS, times, label=labels[i])

    plt.title("График зависимости затрат времени от длины слов для алгоритмов\nпоиска расстояния Дамерау-Левенштейна\n")
    plt.xlabel("Длина строк", fontsize=14)
    plt.ylabel("Время, ns", fontsize=14)
    plt.grid(True)
    plt.legend()

    algs = [matrix_levenshtein, matrix_damerau_levenshtein]
    times_lev_vs_dam = get_times(algs, LENS)

    plt.figure(figsize=(7, 9))
    labels = ['Левенштейн', 'Дамерау-Левенштейн']
    for i, times in enumerate(times_lev_vs_dam):
        plt.plot(LENS, times, label=labels[i])
    plt.title("График зависимости затрат времени от длины слов для матричных\nалгоритмов поиска расстояния Левенштейна и"
              + " Дамерау-Левенштейна\n")
    plt.xlabel("Длина строк", fontsize=14)
    plt.ylabel("Время, ns", fontsize=14)
    plt.grid(True)
    plt.legend()

    plt.show()


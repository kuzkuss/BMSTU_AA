import time
import matplotlib.pyplot as plt
from array import create_random_array, create_zero_array, create_min_array, create_max_array, create_big_data_array
from sort import *

REPEATS = 1000
SIZES = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

def get_time(arr, alg):
    avgTime = 0

    for _ in range(REPEATS):
        start = time.process_time_ns()
        alg(arr)
        avgTime += time.process_time_ns() - start

    avgTime = avgTime / REPEATS

    return int(avgTime)


def get_times_rand(algs):
    print("Подсчёт для произвольного случая:")
    times = [[] for _ in range(len(algs))]

    for size in SIZES:
        print("Подсчёт для массива размером ", size)
        arr = create_random_array(size)
        
        for i, alg in enumerate(algs):
            algTime = get_time(arr, alg)
            times[i].append(algTime)

    return times

def get_times_best(algs):
    print("Подсчёт для лучшего случая:")
    times = [[] for _ in range(len(algs))]

    for size in SIZES:
        print("Подсчёт для массива размером ", size)
        arr_bead = create_zero_array(size)
        arr_counting = create_min_array(size)
        arr_gnome = sorted(create_random_array(size))

        arrs = [arr_bead, arr_counting, arr_gnome]
        
        for i, alg in enumerate(algs):
            algTime = get_time(arrs[i], alg)
            times[i].append(algTime)

    return times

def get_times_worst(algs):
    print("Подсчёт для худшего случая:")
    times = [[] for _ in range(len(algs))]

    for size in SIZES:
        print("Подсчёт для массива размером ", size)
        arr_bead = create_max_array(size)
        arr_counting = create_big_data_array(size)
        arr_gnome = sorted(create_random_array(size), reverse=True)

        arrs = [arr_bead, arr_counting, arr_gnome]
        
        for i, alg in enumerate(algs):
            algTime = get_time(arrs[i], alg)
            times[i].append(algTime)

    return times


def time_measurements():
    sorts = [bead_sort, counting_sort, gnome_sort]

    times_rand = get_times_rand(sorts)
    times_best = get_times_best(sorts)
    times_worst = get_times_worst(sorts)

    labels = ['Бусинами', 'Подсчетом', 'Гномья']
    plt.figure(figsize=(7, 9))
    for i, algTime in enumerate(times_rand):
        plt.plot(SIZES, algTime, label=labels[i])
    plt.title("Зависимость затрат времени от размера массива для алгоритмов \nсортировки (произвольный случай)\n")
    plt.xlabel("Размер массива", fontsize=14)
    plt.ylabel("Время, нс", fontsize=14)
    plt.grid(True)
    plt.legend()

    plt.figure(figsize=(7, 9))
    for i, algTime in enumerate(times_best):
        plt.plot(SIZES, algTime, label=labels[i])
    plt.title("Зависимость затрат времени от размера массива для алгоритмов \nсортировки (лучший случай)\n")
    plt.xlabel("Размер массива", fontsize=14)
    plt.ylabel("Время, нс", fontsize=14)
    plt.grid(True)
    plt.legend()

    plt.figure(figsize=(7, 9))
    for i, algTime in enumerate(times_worst):
        plt.plot(SIZES, algTime, label=labels[i])
    plt.title("Зависимость затрат времени от размера массива для алгоритмов \nсортировки (худший случай)\n")
    plt.xlabel("Размер массива", fontsize=14)
    plt.ylabel("Время, нс", fontsize=14)
    plt.grid(True)
    plt.legend()

    plt.show()

    
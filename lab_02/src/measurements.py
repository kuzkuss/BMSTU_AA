import time
import matplotlib.pyplot as plt
from matrix import *
from multiplication import *

REPEATS = 10
SIZES = [10, 21, 30, 41, 50, 61, 70, 81, 90, 101]

def get_time(mtrx1, mtrx2, alg):
    avgTime = 0

    for _ in range(REPEATS):
        start = time.process_time_ns()
        alg(mtrx1, mtrx2)
        avgTime += time.process_time_ns() - start

    avgTime = avgTime / REPEATS

    return int(avgTime)


def get_times(algs):
    times = [[] for _ in range(len(algs))]

    for size in SIZES:
        print("Подсчёт для матрицы размером ", size, "x", size)
        matr1 = create_random_mtrx(size, size)
        matr2 = create_random_mtrx(size, size)
        
        for i, alg in enumerate(algs):
            algTime = get_time(matr1, matr2, alg)
            times[i].append(algTime)

    return times


def time_measurements():
    algs = [classic_multiplication, winograd_multiplication, optimized_winograd_multiplication]

    times = get_times(algs)

    labels = ['Стандартный', 'Винограда', 'Оптимизированный Винограда']
    plt.figure(figsize=(7, 9))
    for i, algTime in enumerate(times):
        plt.plot(SIZES, algTime, label=labels[i])
    plt.title("График зависимости затрат времени от размера матриц для алгоритмов \nумножения матриц\n")
    plt.xlabel("Размер матриц", fontsize=14)
    plt.ylabel("Время, ns", fontsize=14)
    plt.grid(True)
    plt.legend()

    plt.show()

    
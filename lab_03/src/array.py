import random

def input_array():
    print("Введите массив:")
    arr = list(map(int, input().split()))
    return arr

def print_array(arr):
    print("Отсортированный массив:")
    for i in range(len(arr)):
        print(arr[i], end=' ')

def create_random_array(size):
    return [random.randint(0, 100) for _ in range(size)]

def create_zero_array(size):
    return [0 for _ in range(size)]

def create_min_array(size):
    return [random.randint(0, 10) for _ in range(size)]

def create_max_array(size):
    return [100 for _ in range(size)]

def create_big_data_array(size):
    return [random.randint(size - 10, size) for _ in range(size)]


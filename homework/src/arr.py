from random import randint

def counting_sort():
    """
        Сортировка подсчетом.
    """
    
    size = int(input("Input size: "))       # 1

    arr = []                                # 2

    for _ in range(size):                   # 3
        arr.append(randint(-10, 10))        # 4

    min_elem = min(arr)                     # 5
    max_elem = max(arr)                     # 6
    
    d = min_elem - 1                        # 7
    add_size = max_elem - min_elem + 1      # 8

    add_arr = [0] * add_size                # 9

    for i in range(size):                   # 10
        j = arr[i] - d - 1                  # 11
        add_arr[j] += 1                     # 12
    
    i = 0                                   # 13

    for j in range(add_size):               # 14
        if add_arr[j] > 0:                  # 15
            for _ in range(add_arr[j]):     # 16
                arr[i] = j + d              # 17
                i += 1                      # 18

    return arr


if __name__ == "__main__":
    arr = counting_sort()
    print("Отсортированный массив: ", arr)

def bead_sort(arr):
    size = int(input("Input size: "))

    arr = []

    for _ in range(size):
        arr.append(randint(-10, 10))

    max_elem = max(arr)
    tmp = [0] * max_elem

    for i in range(size):
        for j in range(arr[i]):
            tmp[j] += 1

    for i in range(size):
        count = 0
        for j in range(max_elem):
            if tmp[j] > i:
                count += 1
        arr[size - i - 1] = count

def counting_sort():    
    size = int(input("Input size: "))

    arr = []

    for _ in range(size):
        arr.append(randint(-10, 10))

    min_elem = min(arr)
    max_elem = max(arr)
    
    d = min_elem - 1
    add_size = max_elem - min_elem + 1

    add_arr = [0] * add_size

    for i in range(size):
        j = arr[i] - d - 1
        add_arr[j] += 1
    
    i = 0

    for j in range(add_size):
        if add_arr[j] > 0:
            for _ in range(add_arr[j]):
                arr[i] = j + d
                i += 1

    return arr











def counting_sort(arr):
    count_arr = [0] * (max(arr) + 1)

    for i in range(len(arr)):
        count_arr[arr[i]] += 1

    idx = 0
    for i in range(len(count_arr)):
        for _ in range(count_arr[i]):
            arr[idx] = i
            idx += 1

def gnome_sort(arr):
    i = 1
    while i < len(arr):
        if i == 0 or arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1


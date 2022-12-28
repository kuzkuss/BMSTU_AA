from dataclasses import dataclass
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('tkagg')

NAME_MULTI = "time_multi.csv"
NAME_SINGLE = "time_single.csv"

FILE_MULTI = 1
FILE_SINGLE = 2

COUNT = 0
RESULT = 1

def get_file_data(filename):
    f = open(filename, "r")

    lines = []

    for line in (f.readlines()):
        lines.append(line.split())
    
    f.close

    sizes, result = [], []

    for data in lines:
        sizes.append(int(data[COUNT]))
        result.append(float(data[RESULT]))
    
    return [sizes, result]


def get_graph_result():
    results = []

    title = "Зависимость времени от количества матриц"
    xlabel = "Количество матриц"
    
    label1 = "Последовательная реализация"
    label2 = "Конвейерная реализация"
    
    results.append(get_file_data(NAME_SINGLE)) 
    results.append(get_file_data(NAME_MULTI))

    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(results[0][0], results[0][1], label = label1)
    plot.plot(results[1][0], results[1][1], label = label2)
    plt.legend()
    plt.grid()
    plt.title(title)
    plt.ylabel("Затраченное время(c)")
    plt.xlabel(xlabel)

    plt.show()       

if __name__ == "__main__":
    get_graph_result()


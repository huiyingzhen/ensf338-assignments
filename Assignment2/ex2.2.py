import sys
import matplotlib.pyplot as plt
from time import perf_counter
import json
with open("Assignment 2/ex2.2.json", "r") as j_file:
    file = json.load(j_file)
sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

if __name__ == "main":
    time = []
    for record in file:
        time_start = perf_counter()
        func1(record, 0, len(record))
        time_end = perf_counter()
        time_each = time_end - time_start

        time.append(time_each)
    
    plt.plot(time)
    plt.xticks(len(time))
    plt.show()


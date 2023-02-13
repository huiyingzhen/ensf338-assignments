import sys
import matplotlib.pyplot as plt
from time import perf_counter
import json
with open("/Users/ben/Desktop/ENSF338/assignment2/ensf338-assignments/Assignment2/ex2.2.json", 'r') as f:
    file = json.load(f)
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

if __name__ == "__main__":
    time = []
    numRecords = []
    for record in file:
        time_start = perf_counter()
        func1(record, 0, len(record) - 1)
        time_end = perf_counter()
        time_each = time_end - time_start
        time.append(time_each)
        numRecords.append(file.index(record) + 1)
    
    plt.plot(time)
    plt.title("Time required for Orginal quick sort function")
    plt.xlabel("records")
    plt.ylabel("seconds")
    plt.xticks(numRecords)
    plt.show()


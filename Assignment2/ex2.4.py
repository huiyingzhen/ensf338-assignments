import sys
import matplotlib.pyplot as plt
from time import perf_counter
import json
with open("/Users/ben/Desktop/ENSF338/assignment2/ensf338-assignments/Assignment2/ex2.2.json", 'r') as f:
    file = json.load(f)
sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if (low == high):
        low -= 1
        arr[low], arr[high] = arr[high], arr[low]
    elif (low + 1 == high):
        if arr[low] >= arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
    else:
        func1(arr, low, (high - low) // 2 + low)
        func1(arr, (high - low) // 2 + low + 1, high)
        if (high - low) // 2 + low >= (high - low) // 2 + low + 1:
            pass

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

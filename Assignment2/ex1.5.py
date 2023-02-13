import timeit

def function2(n, prev_results = {}):
    if n == 0 or n == 1:
        return n
    else:
        if n in prev_results:
            return prev_results[n]
        else:
            prev_results[n] = function2(n - 1) + function2(n - 2)
            return prev_results[n]

def function1(n):
    if n == 0 or n == 1:
        return n
    else:
        return function1(n-1) + function1(n-2)

def main():
    #original function
    for i in range(36):
        time1 = timeit.timeit(lambda: function1(i), number=1)
        print("The time it takes to calculate the ",i, "Fibonacci number is:", time1, "seconds")
    
    #function using memoization
    for i in range(36):
        time2 = timeit.timeit(lambda: function2(i), number=1)
        print("The time it takes to calculate the ",i, "Fibonacci number is:", time2, "seconds")

if __name__ == "main":
    main()
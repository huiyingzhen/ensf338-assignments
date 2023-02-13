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

if __name__ == "main":
    n = 35
    calc_f1 = function1(n)
    calc_f2 = function2(n)
    func1 = '''
    def function1(n):
        if n == 0 or n == 1:
            return n
        else:
            return function1(n-1) + function1(n-2)'''

    time_f1 = (timeit.timeit(stmt = func1,
                     number = 1))
    print(time_f1)

    func2 = '''
    def function2(n, prev_results = {}):
        if n == 0 or n == 1:
            return n
        else:
            if n in prev_results:
                return prev_results[n]
            else:
                prev_results[n] = function2(n - 1) + function2(n - 2)
                return prev_results[n]'''
    
    time_f2 = (timeit.timeit(stmt = func2,
                     number = 1))
    print(time_f2)
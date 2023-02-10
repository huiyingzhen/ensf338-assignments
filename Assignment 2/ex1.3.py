def function(n, prev_results = {}):
    if n == 0 or n == 1:
        return n
    else:
        if n in prev_results:
            return prev_results[n]
        else:
            prev_results[n] = function(n - 1) + function(n - 2)
            return prev_results[n]
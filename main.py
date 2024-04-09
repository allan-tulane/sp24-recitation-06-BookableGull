def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        counts[n] += 1
        return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)
    ###TODO
    pass
    

    
def fib_top_down(n, fibs):
    ###TODO
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in fibs:
        return fibs[n]
    else:
        fibs[n] = fib_top_down(n-1, fibs) + fib_top_down(n-2, fibs)
        return fibs[n]

    pass


def fib_bottom_up(n):
    if n <= 1:
        return n
    
    fib_sequence = [0] * (n + 1)
    fib_sequence[1] = 1
    
    for i in range(2, n + 1):
        fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2]
    
    return fib_sequence[n]
    ###TODO
    pass





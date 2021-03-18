def fibonacci(n):  
    """

    calculates the n^th value of the Fibonacci sequence, which is defined by a second-order recurrance formula as below.

    F(n) = F(n-1) + F(n-2)

    >>> fibonacci(0)
    0

    >>> fibonacci(1)
    1

    >>> fibonacci(100)
    354224848179261915075

    >>> fibonacci(-1)
    Traceback (most recent call last):
    ValueError: a sequence is not indexed by n less than zero

    >>> fibonacci(1.0)
    Traceback (most recent call last):
    TypeError: n is not an integer

    :param n: index of the sequence term to be calculated
    :type n: int

    :return: F_n
    :rtype: int

    """

    fib_n, fib_n_minus_1 = 0, 1 #fib_n_minus_1 is just an auxiliary varible, doesn't really refer to F(n-1)

    INDEX = 0

    if n < 0:
        raise ValueError("a sequence is not indexed by n less than zero") 
    elif not isinstance(n, int):
        raise TypeError("n is not an integer") 
    
    while INDEX < n:
        INDEX +=1
        fib_n, fib_n_minus_1 = fib_n + fib_n_minus_1, fib_n

    return fib_n
def is_prime(n):
    
    """
    judge whether an int is prime or not

    >>> is_prime(1)
    False

    >>> is_prime(2)
    True

    >>> is_prime(5)
    True

    >>> is_prime(123)
    False

    >>> is_prime(-1)
    Traceback (most recent call last):
    ValueError: it makes no sense to define a negative or zero as a prime nor not a prime

    >>> is_prime(0)
    Traceback (most recent call last):
    ValueError: it makes no sense to define a negative or zero as a prime nor not a prime

    >>> is_prime(1.0)
    Traceback (most recent call last):
    TypeError: n is not an integer

    :param n: the int to be juded whether it is a prime or not
    :type n: int

    :return: is_prime
    :rtype: bool

    """

    if n <= 0:
        raise ValueError("it makes no sense to define a negative or zero as a prime nor not a prime") 
    elif not isinstance(n, int):
        raise TypeError("n is not an integer") 

    if n == 2:
        return True
    elif n==1 or not n%2:
        return False

    i = 3

    while i*i <= n:
        if not n%i:
            return False
        i += 2

    return True



def prime_factors(n):

    """
    list all the prime factors of n

    >>> prime_factors(1)
    []

    >>> prime_factors(2)
    [2]

    >>> prime_factors(100)
    [2, 5]

    >>> prime_factors(66)
    [2, 3, 11]

    >>> prime_factors(10000)
    [2, 5]

    >>> prime_factors(-1)
    Traceback (most recent call last):
    ValueError: it makes no sense to factorize a negative or zero into primes

    >>> prime_factors(0)
    Traceback (most recent call last):
    ValueError: it makes no sense to factorize a negative or zero into primes

    >>> prime_factors(1.0)
    Traceback (most recent call last):
    TypeError: n is not an integer

    :param n: the int to be factorized
    :type n: int

    :return: factors
    :rtype: list

    """ 

    if n <= 0:
        raise ValueError("it makes no sense to factorize a negative or zero into primes") 
    elif not isinstance(n, int):
        raise TypeError("n is not an integer") 

    factors = []
    i = 3

    if not n%2:
        factors.append(2)

    while i <= n:
        if not n%i and is_prime(i):
            factors.append(i)
        i += 2

    return factors

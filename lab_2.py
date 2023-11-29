import math
def factoriel(n):
    if n < 0 or not(isinstance(n, int)):
        raise ValueError('Нужно неотрицательное целое число')
    else:
        print(math.factorial(n))

factoriel(78)
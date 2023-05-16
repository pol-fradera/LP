def fibs():
    a = 0
    yield a
    b = 1
    while True:
        yield b
        a, b = b, a + b

def roots(x):
    yield x
    y = x
    while True:
        y = 0.5*(y+x/y)
        yield y

def hasDivisors(x,div):
    if (div*div) > x:
        return False
    elif (x%div) == 0:
        return True
    else:
        return hasDivisors(x,div+1)
    
def isPrime(x):
    if x == 0:
        return False
    elif x == 1:
        return False
    else: 
        return not(hasDivisors(x,2))

def primes():
    yield 2
    a = 3
    yield a
    while True:
        a += 2
        if isPrime(a):
            yield a

def is_hamming(x):
    if x == 1:
        return True
    if x%2 == 0:
        return is_hamming(x/2)
    if x%3 == 0:
        return is_hamming(x/3)
    if x%5 == 0:
        return is_hamming(x/5)
    return False

def hammings():
    a = 1
    yield a
    while True:
        a += 1
        if is_hamming(a):
            yield a
def myLength(L):
    return len(L)

def myMaximum(L):
    max = L[0]
    for i in range(1, len(L)):
        if L[i] > max:
            max = L[i]
    return max

def average(L):
    sum = 0
    for x in L:
        sum += x
    return sum/len(L)

def buildPalindrome(L):
    return L[::-1] + L

def remove(L1, L2):
    L = []
    for x in L1:
        if x not in L2:
            L.append(x)
    return L

def flatten(L):
    if len(L) == 0:
        return []
    else:
        x = L[0]
        del L[0]
        if isinstance(x,list):
            return flatten(x) + flatten(L)
        else:
            return [x] + flatten(L)

def oddsNevens(L):
    L1 = []
    L2 = []
    for x in L:
        if x % 2 != 0:
            L1.append(x)
        else:
            L2.append(x)
    return (L1,L2)

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

def primeDivisors(n):
    L = []
    if isPrime(n):
        L.append(n)
    else:
        for x in range(2, n // 2 + 1):
            if isPrime(x) and n % x == 0:
                L.append(x)
    return L
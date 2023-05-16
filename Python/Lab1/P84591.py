def absValue(x):
    if x >= 0:
        return x
    return -x

def power(x,p):
    if p == 0:
        return 1
    return x * power(x,p-1)

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
    
def slowFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return slowFib(n-1) + slowFib(n-2)
    
def quickFib2(a,b,it):
    if it == 0:
        return a
    else:
        return quickFib2(b,a+b,it-1)
    
def quickFib(n):
    return quickFib2(0,1,n) 
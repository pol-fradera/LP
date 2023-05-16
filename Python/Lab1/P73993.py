from functools import reduce
def evens_product(L):
    Le = [x for x in L if x%2 == 0]
    return reduce(lambda acc,y: acc*y, Le, 1)

def reverse(L):
    return reduce(lambda acc,y: [y]+acc, L, [])

def zip_with(f, L1, L2):
    return [f(x,y) for x, y in zip(L1, L2)]

def count_if (f, L):
    return len([x for x in L if f(x)])

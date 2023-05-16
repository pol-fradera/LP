def count_unique(L):
   return len(set(L))

def remove_duplicates(L):
    return list(set(L))

def flatten(L):
    if len(L) == 0:
        return []
    else:
        x = L[0]
        del L[0]
        return x + flatten(L)
    
def flatten_rec(L):
    if len(L) == 0:
        return []
    else:
        x = L[0]
        del L[0]
        if isinstance(x,list):
            return flatten_rec(x) + flatten_rec(L)
        else:
            return [x] + flatten_rec(L)
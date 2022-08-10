#import sys
#sys.setrecursionlimit(10)

def comb(p, n):
    if p == n:
        return 1
    if p == 1:
        return n
    return comb(p-1, n-1) + comb(p, n-1)

print(comb(3, 6))
def somme(n):
    if n == 0:
        return 0
    return n + somme(n-1)


print(somme(3))

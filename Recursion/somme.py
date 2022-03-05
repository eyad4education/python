def somme(x):
    if x == 1:
        return x
    else:
        return x + somme(x-1)


print(somme(3))

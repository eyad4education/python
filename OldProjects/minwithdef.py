def min(x, y):
    if x > y:
        mi = y
    else:
        mi = x
    return mi


print("donner a et b:")
a = int(input())
b = int(input())
print("la plus petit est", min(a, b))

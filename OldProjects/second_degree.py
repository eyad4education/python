from math import *
a = int(input())
b = int(input())
c = int(input())
d = b ** 2 - 4 * a * c
if d < 0:
    print("Ne pas de solution")
elif d == 0:
    x = (-b) / (2*a)
    print("La solution est:", x)
else:
    x1 = (-b - sqrt(d))/(2*a)
    x2 = (-b + sqrt(d))/(2*a)
    print("Les solutions sont:", format(x1, ".2f"), "et", format(x2, ".2f"))

a = int(input())
b = int(input())
if a*b > 0:
    a, b = b, a
else:
    c = a+b
    d = a*b
print(c)
print(d)

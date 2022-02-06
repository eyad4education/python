valid = False
while valid == False:
    n = int(input("Entrer n:"))
    valid = 2<=n<=20
T = n*[int()]
for i in range(n):
    T[i] = int(input("Entrer un nombre: "))


def minimum(T, n):
    min = T[0]
    for i in range(1, n):
        if T[i] < min:
            min = T[i]
    return min


def maximum(T, n):
    max = T[0]
    for i in range(1, n):
        if T[i] > max:
            max = T[i]
    return max


min = minimum(T, n)
max = maximum(T, n)
print(min, "  ", max)

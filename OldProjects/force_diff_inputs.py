def saisie():
    global n
    v = False
    while v == False:
        n = int(input("Donner n: "))
        v = 2 <= n <= 100


def seq(x, y):
    v = False
    i = 0
    while v == False:
        con = False
        if T[i] == x:
            con = True
        i += 1
        v = con == True or i == y
    return con


def completer(n):
    global T
    T[0] = int(input("Donner l'element nemuro 1: "))
    for i in range(1, n):
        v = False
        while v == False:
            print("Donner l'element nemuro", i+1, ": ", end="")
            T[i] = int(input())
            v = seq(T[i], i) == False


saisie()
T = [int()] * n
completer(n)
print(T)

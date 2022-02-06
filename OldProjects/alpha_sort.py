def saisie():
    global n
    v = False
    while v == False:
        n = int(input("Donner n: "))
        v = 2 <= n <= 100


def completer(n):
    global T
    for i in range(n):
        v = False
        while v == False:
            print("Donner la caractere numero", i+1, ": ", end="")
            T[i] = input("")
            v = (len(T[i]) == 1) and (64 < ord(T[i]) < 91)


def trier(T, n):
    v = False
    while v == False:
        con = False
        for i in range(n-1):
            if ord(T[i]) > ord(T[i+1]):
                x = T[i]
                T[i] = T[i+1]
                T[i+1] = x
                con = True
        v = con == False


saisie()
T = [str()] * n
completer(n)
trier(T, n)
print(T)
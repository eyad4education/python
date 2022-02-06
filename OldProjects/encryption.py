from random import randint


def saisir():
    global n
    while True:
        print("Entrer n: ", end="")
        n = int(input())
        if 1 <= n <= 20:
            break
    # valid = False
    # while valid == False:
    #     n = int(input("Enter n: "))
    #     valid = 3 <= n <= 20


def remplir(n):
    global Td
    for i in range(n):
        valid = False
        while valid == False:
            print("Enter Letter Number", i+1, ": ", end="")
            Td[i] = str(input())
            valid = Td[i].isalpha() == True and len(Td[i]) == 1 and Td[i].isupper() == True


def liez(Tf, n):
    s = ""
    for i in range(n):
        s = s + str(Tf[i])
    return s


def reverser(Td, n):
    global Tf
    for i in range(n):
        x = ord(Td[i])
        rv = (x % 10 * 10) + (x // 10)
        Tf[i] = chr(rv)
    crp = liez(Tf, n)
    print(crp)


saisir()
Td = [str()]*n
Tf = [str()]*n
remplir(n)
reverser(Td, n)
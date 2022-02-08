import numpy as np


def donner():
    global l, c
    l = int(input("Donner L: "))
    c = int(input("Donner C: "))


def completer(l, c):
    global m
    for j in range(l):
        for i in range(c):
            v = False
            while v == False:
                print("Donner l'element ligne", j+1, "colonne", i+1, ": ")
                m[j, i] = int(input())
                v = m[j, i] > 0


def executer(m, l, c):
    for j in range(l):
        for i in range(c):
            if somme(m, l, c, j, i) == False:
                print("Element", m[j, i], "ligne", j+1, "colonne", i+1)


def somme(m, l, c, j, i):
    chl = ""
    chc = ""
    for y in range(l):
        chl += str(m[y, i])
    for x in range(c):
        chc += str(m[j, x])
    nbl = 0
    nbc = 0
    for a in range(len(chl)):
        nbl += int(chl[a])
    for a in range(len(chc)):
        nbc += int(chc[a])
    if nbl == nbc:
        okay = False
    else:
        okay = True
    return okay


donner()
m = np.array([[int()]*c]*l)
completer(l, c)
executer(m, l, c)

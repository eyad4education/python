import numpy as np


def saisir():
    global l, c, m
    l = int(input())
    c = int(input())
    m = np.array([[float()]*c]*l)
    for j in range(l):
        for i in range(c):
            print("Donner l'element ", j+1, ",", i+1, ": ", end="")
            m[j, i] = float(input())


def comp(m, l, c):
    global max, min
    max = m[0, 0]
    min = m[0, 0]
    for j in range(l):
        for i in range(c):
            if m[j, i] > max:
                max = m[j, i]
            elif m[j, i] < min:
                min = m[j, i]


saisir()
comp(m, l, c)
print("max: ", max)
print("min: ", min)
from random import randint
import numpy as np


def donner():
    global nl, nc, n
    v = False
    while v == False:
        nl = int(input("Donner nl:"))
        v = 2 <= nl <= 10000
    v = False
    while v == False:
        nc = int(input("Donner nc:"))
        v = 2 <= nc <= 20
    v = False
    while v == False:
        n = int(input("Donner n:"))
        v = 2 <= n <= 20


def isAlphaMaj(ch):
    isAM = True
    i = 0
    while i < len(ch) and isAM:
        if ord(ch[i]) > 90 or ord(ch[i]) < 65:
            isAM = False
        i += 1
    return isAM


def compt_m(nl, nc):
    global m
    for j in range(nl):
        for i in range(nc):
            m[j, i] = chr(randint(65, 90))


def compt_t(nc, n):
    global t
    for i in range(n):
        v = False
        while v == False:
            t[i] = str(input("Donner un mot: "))
            v = isAlphaMaj(t[i]) and len(t[i]) == nc


def tri(ch):
    list = [str()] * (len(ch))
    for i in range(len(ch)):
        list[i] = ch[i]
    v = False
    while v == False:
        estTrier = True
        for i in range(len(ch)-1):
            if ord(list[i]) > ord(list[i+1]):
                swap = list[i]
                list[i] = list[i+1]
                list[i+1] = swap
                estTrier = False
        v = estTrier
    trieCH = ""
    for i in range(len(ch)):
        trieCH += list[i]
    return trieCH


def compt_tn(m, t, nl, nc, n):
    global tn
    for j in range(nl):
        word = ""
        for i in range(nc):
            word += m[j, i]
        for z in range(nl):
            for y in range(n):
                s = 0
                if tri(t[y]) == tri(word):
                    s += 1
                tn[y] = s


donner()
m = np.array([[str] * nc] * nl)
compt_m(nl, nc)
t = [str()] * n
compt_t(nc, n)
tn = [int()] * n
compt_tn(m, t, nl, nc, n)
print(tn)

import numpy as np
from random import randint


def saisir():
    global l, c
    v = False
    while v == False:
        l = int(input("Donner la nombre de lignes: "))
        v = l <= 10
    v = False
    while v == False:
        c = int(input("Donner la nombre de colones: "))
        v = c <= 10


def remplir_alea(lignes, colones):
    global m
    for j in range(lignes):
        for i in range(colones):
            m[j, i] = randint(100, 999)


def somme_chiffres(matrice, lignes, colones):
    ch = str(matrice[lignes, colones])
    somme = 0
    for i in range(len(ch)):
        somme += int(ch[i])
    return somme


def affiche(matrice, lignes, colones):
    for j in range(lignes):
        for i in range(colones):
            matrice[j, i] = somme_chiffres(matrice, j, i)
            print("la somme de case [", j+1, ",", i +1, "] chiffres est:", matrice[j, i])


saisir()
m = np.array([[int()]*c]*l)
remplir_alea(l, c)
affiche(m, l, c)
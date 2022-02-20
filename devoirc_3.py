import numpy as np


def sumSpace(string):
    space = " "
    breakout = False
    sum = 0
    if string.find(space) == -1 and string.find(space) != len(string)-1:
        breakout = True
    i = 0
    while breakout == False and i < len(string):
        if string[i] == space:
            sum += 1
        i += 1
    return sum


def ch_t(string):
    global t
    old = 0
    newstring = string
    for i in range(sumSpace(string)+1):
        if newstring.find(" ") != -1:
            index = newstring.find(" ")
        else:
            index = len(string)
        t[i] = newstring[0:index]
        old = newstring.find(" ")+1
        newstring = newstring[old:len(newstring)]


def sorting(n):
    global t, m
    v = False
    while v == False:
        for i in range(n-1):
            sorted = True
            ch1 = t[i]
            ch2 = t[i+1]
            if ch1[0].upper() > ch2[0].upper():
                swap = t[i]
                t[i] = t[i+1]
                t[i+1] = swap
                sorted = False
        v = sorted == True
    v = False
    while v == False:
        for i in range(n-1):
            sorted = True
            ch1 = m[0][i]
            ch2 = m[0][i+1]
            if ch1[0].upper() > ch2[0].upper():
                swap = m[0][i]
                m[0][i] = m[0][i+1]
                m[0][i+1] = swap
                sorted = False
        v = sorted == True


v = False
while v == False:
    n = int(input("Give n: "))
    v = 1 <= n <= 10
m = np.array([[str]*n]*2)

for i in range(n):
    for j in range(2):
        if j == 0:
            m[j][i] = str(input("give a word in french: "))
        elif j == 1:
            m[j][i] = str(input("give its translation in english: "))
# m = [["ici", "facile", "donc", "donner"], ["here", "easy", "so", "give"]]
t = [str()] * n
phf = str(input("give the sentence you want to translate: "))
if phf[len(phf)-1] == " ":
    phf = phf[0:len(phf)-1]
ch_t(phf)
sorting(n)
spaces = sumSpace(phf)
if spaces == 0:
    i = 0
    found = False
    phg = ""
    v = False
    while v == False:
        if m[0][i] == phf:
            output = m[1][i]
            found = True
        i += 1
        v = found == True or i == n
elif spaces > 0:
    phg = ""
    for i in range(n):
        for j in range(n):
            if m[0][i] == t[j]:
                phg += m[1][i] + " "


print("the translation from french to english is:", phg)

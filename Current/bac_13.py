def saisir():
    global n
    v = False
    while not v:
        n = int(input("donner n: "))
        v = n <= 50


def Verif(ch):
    con = True
    i = 0
    while (con) and (i < len(ch)):
        if (ch[i] < "A" or ch[i] > "Z") and (ch[i] < "a" or ch[i] > "z") and ch[i] != " ":
            con = False
        i = i + 1
    return con


def remplir(np1, n):
    F = open(np1, "w")
    for i in range(n):
        v = False
        while not v:
            ch = str(input(f"donner phrase {i+1}: "))
            v = Verif(ch)
        F.write(ch + "\n")
    F.close()


def former(t, x):
    ch = ""
    for i in range(x):
        ch = ch + t[i]
    return ch


def crypting(c, x):
    if chr(ord(c)+x) >= "Z" and chr(ord(c)+x) < "a" and c < "a":
        nc = chr(ord(c)+(x%26)-26)
    else:
        if chr(ord(c)+x) >= "z":
            nc = chr(ord(c)+(x%26)-26)
        else:
            nc = chr(ord(c)+(x%26))
    return nc


def crypter(np1, np2, n):
    A = open(np1, "r")
    B = open(np2, "w")
    for i in range(n):
        ch = A.readline().rstrip()
        t = [str()] * len(ch)
        for k in range(len(ch)):
            t[k] = ch[k]
        x = 1
        for j in range(len(ch)):
            if t[j] != " ":
                t[j] = crypting(t[j], x)
            else:
                x = x + 1
        ch = former(t, len(ch))
        B.write(ch + "\n")
    A.close()
    B.close()


saisir()
np1 = "Phrases.txt"
remplir(np1, n)
np2 = "Ph_Crypt.txt"
crypter(np1, np2, n)

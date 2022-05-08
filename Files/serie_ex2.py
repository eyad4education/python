from time import sleep


def saisie():
    global n
    v = False
    while not v:
        n = int(input("donner n: "))
        v = 3 <= n <= 15


def fixer(np, n):
    zeros = ""
    for i in range(n):
        zeros += "0"
    F = open(np, "r")
    t = [str()] * n
    i = 0
    for k in range(n):
        ch = F.readline().rstrip()
        if ch == "":
            t[i] = zeros
        if len(ch) > n:
            t[i] = ch[0:n]
            i += 1
        elif len(ch) < n:
            t[i] = zeros[:n-(len(ch))] + ch
            i += 1
        else:
            t[i] = ch
            i += 1
    F.close()
    F = open(np, "w")
    for k in range(i):
        F.write(t[k] + "\n")
    F.close()
    sleep(3)


def remplir_mat(m, np, n):
    F = open(np, "r")
    for j in range(n):
        ch = F.readline().rstrip()
        for i in range(n):
            m[j][i] = ch[i]
    F.close()


def trier_mat(m, n):
    for j in range(n):
        con = True
        v = False
        while not v:
            con = True
            for i in range(n-1):
                if int(m[j][i]) < int(m[j][i+1]):
                    swap = m[j][i]
                    m[j][i] = m[j][i+1]
                    m[j][i+1] = swap
                    con = False

            v = con


def former(m, a, n):
    ch = ""
    for i in range(n):
        ch += m[i][a]
    return ch


def remplir_fch(m, np, n):
    F = open(np, "w")
    for j in range(n):
        ch = former(m, j, n)
        F.write(ch + "\n")
    F.close()


saisie()
np = "source.txt"
F = open(np, "w")
F.write("2110\n1401869\n90181\n111\n94172\n")
F.close()
sleep(3)
fixer(np, n)
m = [[int() for i in range(n)] for i in range(n)]
remplir_mat(m, np, n)
trier_mat(m, n)
remplir_fch(m, np, n)

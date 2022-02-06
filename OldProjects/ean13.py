def saisie():
    global n, ch
    while True:
        n = input("Donner n: ")
        if len(n) == 13 and n.isnumeric() == True:
            ch = n
            break


def div(ch):
    global cc, q, r, p
    cc = ch[len(ch)-1:len(ch)]
    q = ch[0:len(ch)-1]
    s = 0
    for i in range(len(q)):
        if not int(q[i]) % 2 == 0:
            s = s + int(q[i])*3
    r = s % 10
    p = 10 - r

saisie()
div(ch)
print(r)
print(p)

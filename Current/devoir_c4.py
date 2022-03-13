def former(m, j, nc):
    ch = ""
    for i in range(nc):
        ch += m[j][i]
    return ch


def trier(ch):
    tempt = [str()] * len(ch)
    for i in range(len(ch)):
        tempt[i] = ch[i]
    v = False
    while not v:
        con = True
        for i in range(len(ch)-1):
            if tempt[i] > tempt[i+1]:
                swap = tempt[i]
                tempt[i] = tempt[i+1]
                tempt[i+1] = swap
                con = False
        v = con
    och = ""
    for i in range(len(ch)):
        och += tempt[i]
    return och


def anagrame(m, t, tn, nl, nc, n):
    for i in range(n):
        for j in range(nl):
            ch1 = trier(former(m, j, nc))
            ch2 = trier(t[i])
            if ch1 == ch2:
                tn[i] = tn[i] + 1


nl = 13
nc = 5
n = 4
t = ["POULE", "CHIEN", "SORTE", "POIRE"]
m = [["P", "R", "O", "I", "E"], ["P", "E", "T", "I", "T"], ["C", "H", "I", "N", "E"], ["L", "O", "U", "P", "E"], ["C", "H", "E", "N", "I"], ["R", "E", "S", "T", "O"], ["N", "I",
                                                                                                                                                                        "C", "H", "E"], ["S", "T", "O", "R", "E"], ["F", "O", "I", "R", "E"], ["P", "O", "U", "E", "L"], ["R", "O", "T", "E", "S"], ["P", "I", "E", "R", "O"], ["T", "O", "R", "S", "E"]]
tn = [int()] * n
anagrame(m, t, tn, nl, nc, n)
max = 0
for i in range(1, n):
    if tn[i] > tn[max]:
        max = i
print("Le mot qui a le plus grand nombre d'anagramme est: " + t[max])

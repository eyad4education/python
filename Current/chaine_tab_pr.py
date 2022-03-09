def chaine_tab(ch):
    global t
    v = False
    while not v:
        if ch[len(ch)-1:len(ch)] == " ":
            ch = ch[:len(ch)-1] + ch[len(ch):]
        else:
            v = 1
    nbw = 1
    for i in range(len(ch)-1):
        if ch[i] == " ":
            nbw += 1
    t = [str()] * nbw
    ch += " "
    for i in range(nbw):
        t[i] = ch[0:ch.find(" ")]
        ch = ch[:0] + ch[ch.find(" ")+1:]


chaine_tab("abc okay test       ")
print(t)

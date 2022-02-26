def estChance(number):
    est = True
    number = number[2:len(number)]
    x = int(number[0])
    y = int(number[0])+1
    its = 0
    i = 0
    while i < len(number) and its < 4:
        if int(number[i]) == y-1:
            its += 1
            y += 1
        else:
            its = 0
            x = int(number[i])
            y = int(number[i])+1
            i -= 1
        i += 1
    if its < 4:
        est = False
    return est


if estChance("22096789"):
    print("CHANCE")
else:
    print("NE PAS CHANCE")

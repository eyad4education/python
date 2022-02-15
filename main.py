from random import randint


def fill():
    global n
    v = False
    while v == False:
        n = int(input("Enter n: "))
        v = n > 2


def complete(n):
    global tnumber
    tnumber[0] = randint(1, 100)
    for i in range(1, n):
        v = False
        while v == False:
            tnumber[i] = randint(1, 100)
            v = isDiff(tnumber, tnumber[i], i)


def isDiff(table, element, position):
    isDifferent = True
    i = 0
    v = False
    while v == False:
        if table[i] == element:
            isDifferent = False
        i += 1
        v = (isDifferent == False) or (i == position)
    return isDifferent


def generate(tnumber, n):
    global tnature
    for i in range(n):
        e = {}
        e["number"] = tnumber[i]
        div(tnumber[i])
        e["nbdivs"] = numberDivs
        e["nat"] = numberNature
        tnature[i] = e


def div(number):
    global numberDivs, numberNature
    numberDivs = 1
    sum = 0
    for i in range(1, number//2+1):
        if number % i == 0:
            numberDivs += 1
            sum += i
    if sum == number:
        numberNature = "Perfect"
    elif sum < number:
        numberNature = "Deficient"
    else:
        numberNature = "Abundant"


def show(tnature, n):
    for i in range(n):
        e = tnature[i]
        print(e["number"], " ", e["nbdivs"], " ", e["nat"])


fill()
tnumber = [int()] * n
complete(n)
tnature = [{}] * n
generate(tnumber, n)
show(tnature, n)

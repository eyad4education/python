def isAlpha(string):
    isA = True
    i = 0
    while i < len(string) and isA:
        if not("A" <= string[i] <= "Z" or "a" <= string[i] <= "z"):
            isA = False
        i += 1
    return isA


string = str(input("give a word: "))
while not isAlpha(string):
    string = str(input("give a word (only alphabetic letters): "))
print(string)

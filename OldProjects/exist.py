T = [1, 2, 3, 5]
n = 4
number = 3
itExists = False
i = 0
while i < 4 and itExists == False:
    if T[i] == number:
        itExists = True
    i += 1
if itExists:
    print(number, "Exists in this list.")
else:
    print(n, "Does not exist in this list.")

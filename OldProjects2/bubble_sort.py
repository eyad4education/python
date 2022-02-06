n = 9
t = [1, 5, 2, 8, 4, 9, 3, 7, 6]
tmp = 0
while True:
    con = False
    for i in range(n-1):
        if t[i] > t[i+1]:
            tmp = t[i]
            t[i] = t[i+1]
            t[i+1] = tmp
            con = True
    if con == False:
        break
for i in range(n):
    print(t[i], end=" ")
print("\n")
print("\n")
x = input("Press enter to exit...")

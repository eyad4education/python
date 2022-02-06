x = False
while x == False:
    n = int(input())
    x = 3 <= n <= 40
t = [float] * n
for i in range(n):
    x = False
    while x == False:
        t[i] = float(input())
        x = 0 <= t[i] <= 20
x = False
while x == False:
    con = False
    for i in range(n-1):
        if t[i] < t[i+1]:
            y = t[i]
            t[i] = t[i+1]
            t[i+1] = y
            con = True
    x = con == False
print("1.", format(t[0], '.2f'))
print("2.", format(t[1], '.2f'))
print("3.", format(t[2], '.2f'))
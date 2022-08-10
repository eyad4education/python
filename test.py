n = 3
m = [[5,7,3],
     [3,5,7],
     [7,3,5]]
t = [int()] * (n*2 + 2)

def mat_hero(m, n, a):
    sum = 0
    for i in range(n):
        sum = sum + m[a][i]
    return sum
def mat_vert(m, n, a):
    sum = 0
    for i in range(n):
        sum = sum + m[i][a]
    return sum
def diag_un(m, n):
    sum = 0
    j = 0
    for i in range(n):
        sum = sum + m[j][i]
        j = j + 1
    return sum
def diag_deux(m, n):
    sum = 0
    for i in range(n):
        sum = sum + m[i][n-1-i]
    return sum
def matrice_perfet(m, n):
    y = n*2 + 2
    for i in range(n):
        t[i] = mat_hero(m,n,i)
    for i in range(n*2):
        t[i] = mat_vert(m, n, i-n)
    t[y-2] = diag_un(m,n)
    t[y-1] = diag_deux(m,n)
    print(t)
    con = True
    i = 1
    while con and i < y:
        if not t[0] == t[i-1]:
            con = False
        i = i + 1
    return con


print(matrice_perfet(m, n))

    
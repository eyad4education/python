n = 3
e = n*n
arr = [[5,3,4],[2,1,6],[7,9,8]]
t = [0]*e
x = 0
# Transfering a 2D array to 1D array
for j in range(n):
    for i in range(n):
        if x < e:
            t[x] = arr[j][i]
            x+=1
# Sorting the 1D array using Bubble sort algorithm
v = False
while v == False:
    con = False
    for i in range(e-1):
        if t[i] > t[i+1]:
            w = t[i]
            t[i] = t[i+1]
            t[i+1] = w
            con = True
    v = con == False
# Transfering a 1D array to 2D array
x = 0
for j in range(n):
    for i in range(n):
        if x < e:
            arr[j][i] = t[x]
            x+=1
for i in arr:
    print(i)
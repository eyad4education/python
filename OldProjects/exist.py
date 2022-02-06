T = [1, 2, 3, 5]
n = 4
x = 0
for i in range(len(T)):
    if T[i] == n:
        x = x + 1
if x == 0:
    print("Nope!",n,"Doesn't exist in",T)
else:
    print("Yes!",n,"Exists in",T)
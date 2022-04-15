for x in range(1, 101):
    y = 0
    for i in range(2, x//2 + 1):
        if x % i == 0:
            y += 1
            break
    if y == 0 and x != 1:
        print(x, end=" ")

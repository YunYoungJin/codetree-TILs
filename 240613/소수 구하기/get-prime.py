n = int(input())

for i in range(2, n + 1):
    pn = True
    for j in range(2, i):
        if i % j == 0:
            pn = False
    if pn:
        print(i, end=' ')
x = list(map(int, input().split()))
cnt = 0
x.sort()

while not (x[2] - x[1] == 1 and x[1] - x[0] == 1):
    d1, d2 = x[1] - x[0], x[2] - x[1]
    
    if d1 == 2:
        x[2] = x[0] + 1
    elif d2 == 2:
        x[0] = x[1] + 1
    elif d1 == 1:
        x[0] = x[1] + 2
    elif d2 == 1:
        x[2] = x[1] - 2
    else:
        x[0] = x[1] + 2

    x.sort()
    cnt += 1

print(cnt)
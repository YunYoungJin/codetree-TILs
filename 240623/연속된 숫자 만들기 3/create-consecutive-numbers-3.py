x = list(map(int, input().split()))
cnt = 0

d1, d2 = x[1] - x[0], x[2] - x[1]

if d1 == 1 and d2 == 1:
    cnt = 0
elif d1 > d2:
    cnt = d1 - 1
else:
    cnt = d2 - 1

print(cnt)
n = int(input())

line = dict()

for _ in range(n):
    x, y = map(int, input().split())

    if x not in line:
        line[x] = y
    else:
        if y < line[x]:
            line[x] = y

ans = 0
for value in line.values():
    ans += value
print(ans)
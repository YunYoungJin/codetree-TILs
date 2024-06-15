n = int(input())
line = [0] * 2001
offset = 1000
pos = offset

for _ in range(n):
    x, LR = input().split()
    x = int(x)
    if LR == 'L':
        for i in range(pos, pos - x -1, -1):
            line[i] += 1
        pos = pos - x
    else:
        for i in range(pos, pos + x + 1):
            line[i] += 1
        poas = pos + x
cnt = 0
for i in range(len(line)):
    if line[i] >= 2:
        cnt += 1
print(cnt)
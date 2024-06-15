n = int(input())
line = [''] * 200001
checked = [0] * 200001
offset = 100000
pos = offset

for _ in range(n):
    x, LR = input().split()
    x = int(x)
    if LR == 'L':
        for i in range(pos, pos - x, -1):
            if line[i] != 'G':
                line[i] = 'W'
            checked[i] += 1
            if checked[i] == 4:
                line[i] = 'G'
        pos = pos - x + 1
    else:
        for i in range(pos, pos + x):
            if line[i] != 'G':
                line[i] = 'B'
            checked[i] += 1
            if checked[i] == 4:
                line[i] = 'G'
        pos = pos + x - 1

print(line.count('W'), line.count('B'), line.count('G'))
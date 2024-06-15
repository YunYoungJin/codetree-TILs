n = int(input())
line = [''] * 200001
pos = 100000

for _ in range(n):
    x, LR = input().split()
    x = int(x)
    if LR == 'L':
        for i in range(pos-x+1, pos+1):
            line[i] = 'W'
        pos = pos - x + 1
    else:
        for i in range(pos, pos + x):
            line[i] = 'B'
        pos = pos + x - 1

print(line.count('W'), line.count('B'))
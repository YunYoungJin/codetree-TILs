n = int(input())
line = [''] * 200001
white = [0] * 200001
black = [0] * 200001
pos = 100000

for _ in range(n):
    x, LR = input().split()
    x = int(x)
    if LR == 'L':
        for i in range(pos-x+1, pos+1):
            line[i] = 'W'
            white[i] += 1
        pos = pos - x + 1
    else:
        for i in range(pos, pos + x):
            line[i] = 'B'
            black[i] += 1
        pos = pos + x - 1

for i in range(len(line)):
    if white[i] >= 2 and black[i] >= 2:
        line[i] = 'G'

print(line.count('W'), line.count('B'), line.count('G'))
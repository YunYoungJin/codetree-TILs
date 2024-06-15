n = int(input())
offset = 100
line = [0] * 201
for _ in range(n):
    x1, x2 = map(int, input().split())
    for i in range(x1 + offset, x2 + offset):
        line[i] += 1
print(max(line))
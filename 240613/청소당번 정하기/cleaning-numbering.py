n = int(input())
x = y = z = 0

for i in range(1, n + 1):
    if i % 12 == 0:
        z += 1
        continue
    elif i % 3 == 0:
        y += 1
        continue
    elif i % 2 == 0:
        x += 1
print(x, y, z)
n = int(input())

for i in range(n):
    for j in range(11 + 2 * i, 11 + 2 * (i + n), 2):
        print(j, end=' ')
    print()
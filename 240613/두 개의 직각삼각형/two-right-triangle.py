n = int(input())

for i in range(n):
    for j in range(n - i, 0, -1):
        print('*', end='')
    for k in range(2 * i):
        print(' ', end='')
    for j in range(n - i, 0, -1):
        print('*', end='')
    print()
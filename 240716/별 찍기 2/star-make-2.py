n, m = map(int, input().split())

def Print1(n):
    for i in range(1, n // 2 + 2):
        print('*' * i)
    for i in range(n // 2, 0, -1):
        print('*' * i)
    print()

def Print2(n):
    for i in range(1, n // 2 + 2):
        print(' ' * (n // 2 + 1 - i) + '*' * i)
    for i in range(n // 2, 0, -1):
        print(' ' * (n // 2 + 1 - i) + '*' * i)
    print()

def Print3(n):
    for i in range(n // 2 + 1):
        print(' ' * i + '*' * (n - 2 * i))
    for i in range(n // 2 - 1, -1, -1):
        print(' ' * i + '*' * (n - 2 * i))
    print()

def Print4(n):
    for i in range(n // 2 + 1, 1, -1):
        print(' ' * (n // 2 + 1 - i) + '*' * i)
    for i in range(1, n // 2 + 2):
        print(' ' * (n // 2 ) + '*' * i)
    print()


if m == 1:
    Print1(n)
elif m == 2:
    Print2(n)
elif m == 3:
    Print3(n)
else:
    Print4(n)
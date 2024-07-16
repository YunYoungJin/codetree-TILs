n, m = map(int, input().split())

def Print1(n):
    for i in range(1, n + 1):
        print('*' * i)

def Print2(n):
    for i in range(n, 0, -1):
        print('*' * i)

def Print3(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))


if m == 1:
    Print1(n)
elif m == 2:
    Print2(n)
elif m == 3:
    Print3(n)
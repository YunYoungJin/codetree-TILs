n = int(input())
cnt = 'A'

for i in range(n):
    for _ in range(2 * i):
        print(' ', end='')
    for j in range(n - i, 0, -1):
        print(cnt, end=" ")
        cnt = chr(ord(cnt) + 1)
        if ord(cnt) > ord('Z'):
            cnt = 'A'
    print()
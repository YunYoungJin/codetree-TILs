n = int(input())
cnt = 'A'

for i in range(1, n + 1):
    for _ in range(i):
        print(cnt, end="")
        if cnt == 'Z':
            cnt = 'A'
        else:
            cnt = chr(ord(cnt) + 1)
    print()
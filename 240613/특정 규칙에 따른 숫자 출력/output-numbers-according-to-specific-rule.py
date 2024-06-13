n = int(input())
cnt = 1

for i in range(n):
    for _ in range(i):
        print(' ', end=' ')
    for j in range(n - i, 0, -1):
        print(cnt, end=' ')
        cnt += 1
        if cnt == 10:
            cnt = 1
    print()
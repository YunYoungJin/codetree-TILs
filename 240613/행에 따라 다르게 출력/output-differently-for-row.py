n = int(input())

cnt = 0

for i in range(1, n + 1):
    for j in range(n):
        if i % 2 == 1:
            cnt += 1
            print(cnt, end=' ')
        if i % 2 == 0:
            cnt += 2
            print(cnt, end=' ')
    print()
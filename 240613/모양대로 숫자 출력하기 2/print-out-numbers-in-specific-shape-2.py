n = int(input())
cnt = 2

for _ in range(n):
    for _ in range(n):
        print(cnt, end=' ')
        cnt += 2
        if cnt == 10:
            cnt = 2
    print()
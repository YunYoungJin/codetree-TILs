n = int(input())
cnt = 1
for i in range(1, n + 1):
    if i % 2 == 1:
        for j in range(n):
            print(n * (i - 1) + 1 + j, end=' ')
    else:
        for k in range(n):
            print(n * i - k, end=' ')
    print()
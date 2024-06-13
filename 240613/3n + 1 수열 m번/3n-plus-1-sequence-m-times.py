m = int(input())

for _ in range(m):
    n = int(input())
    cnt = 0

    while True:
        if n == 1:
            print(cnt)
            break
        elif n % 2 == 0:
            n //= 2
        elif n % 2 == 1:
            n = 3 * n + 1
        cnt += 1
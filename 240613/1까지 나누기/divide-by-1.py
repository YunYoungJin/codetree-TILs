n = int(input())
i = 0
cnt = 0
while True:
    i += 1
    n //= i
    cnt += 1
    if n <= 1:
        print(cnt)
        break
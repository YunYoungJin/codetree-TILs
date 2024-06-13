n = int(input())
cnt = 0
while True:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    cnt += 1
    if n == 1:
        break
print(cnt)
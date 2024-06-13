n = int(input())
arr = []
i = 1
cnt = 0

while True:
    arr.append(n * i)
    if (n * i) % 5 == 0:
        cnt += 1
    if cnt == 2:
        break
    i += 1
print(*arr)
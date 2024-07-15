n = int(input())
arr = list(map(int, input().split()))

ans = 0
for i in range(1, n):
    if i != n - 1:
        if arr[i - 1] == 0:
            for j in range(i - 1, i + 2):
                arr[j] = (1 if arr[j] == 0 else 0)
            ans += 1
    else:
        if arr[i - 1] == 0:
            for j in range(i - 1, i + 1):
                arr[j] = (1 if arr[j] == 0 else 0)
            ans += 1

if arr[-1] == 0:
    print(-1)
else:
    print(ans)
n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))

ans = 100001

sum_val = 0
j = 1

for i in range(1, n + 1):
    while j <= n:
        if sum_val + arr[j] < s:
            sum_val += arr[j]
            j += 1
        else:
            ans = min(ans, j - i + 1)
            break

    sum_val -= arr[i]

if ans == 100001:
    print(-1)
else:
    print(ans)
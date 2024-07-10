n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
ans = 0

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        tmp_sum = prefix_sum[j] - prefix_sum[i - 1]
        if tmp_sum == k:
            ans += 1

print(ans)
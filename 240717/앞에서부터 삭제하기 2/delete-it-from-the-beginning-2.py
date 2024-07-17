n = int(input())
arr = list(map(int ,input().split()))

prefix_sum = [0] * (n + 1)
min_val = [10001] * (n + 1)

for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + arr[i]

for i in range(n - 1, -1, -1):
    min_val[i] = min(min_val[i + 1], arr[i])

ans = 0
for k in range(1, n - 1):
    tmp_sum = prefix_sum[n] - prefix_sum[k]
    ans = max(ans, (tmp_sum - min_val[k])/(n - k - 1))

print(f"{ans:.2f}")
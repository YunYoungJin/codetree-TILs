n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

ans = 0
prefix_sum = [0] * (n + 1)
first = [-1] * 7

for i in range(1, n + 1):
    prefix_sum[i] = (prefix_sum[i - 1] + arr[i - 1]) % 7

    if first[prefix_sum[i]] == -1:
        first[prefix_sum[i]] = i

for i in range(1, n + 1):
    ans = max(ans, i - first[prefix_sum[i]])

print(ans)
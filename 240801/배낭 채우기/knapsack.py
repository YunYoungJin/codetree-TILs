n, m = map(int, input().split())
jewels = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

dp = [0] * (m + 1)

for weight, value in jewels:
    for w in range(m, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[m])
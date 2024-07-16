n = int(input())
segments = [(0, 0)] + [
    tuple(map(int, input().split()))
    for _ in range(n)
]

segments.sort()

# i번째 선분 까지 고려했을 때, 겹치지 않은 가장 많은 수의 선분
dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    x1, x2 = segments[i]

    for j in range(1, i):
        prev_x1, prev_x2 = segments[j]

        if x1 <= prev_x2:
            dp[i] = max(dp[j], dp[i])
        else:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp[n])
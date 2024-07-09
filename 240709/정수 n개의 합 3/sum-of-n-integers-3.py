n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = 0
prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] \
                        - prefix_sum[i - 1][j - 1] + grid[i - 1][j - 1]

def in_range(x, y):
    return x <= n and y <= n

for i in range(1, n + 1):
    for j in range(1, n + 1):
        x1, y1 = i, j
        x2, y2 = i + k - 1, j + k - 1
        if not in_range(x2, y2):
            break
        ans = max(ans, prefix_sum[x2][y2] - prefix_sum[x2][y1 - 1] - prefix_sum[x1 - 1][y2] + \
                prefix_sum[x1 - 1][y1 - 1])

print(ans)
n, m, p = map(int, input().split())
grid = [
    list(input())
    for _ in range(n)
]

grid_cnt = []
for i in range(n):
    tmp = []
    for j in range(m):
        if grid[i][j] == 'a':
            tmp.append([1, 0, 0])
        elif grid[i][j] == 'b':
            tmp.append([0, 1, 0])
        else:
            tmp.append([0, 0, 1])
    grid_cnt.append(tmp)

prefix_sum = [[[0, 0, 0] for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(3):
            prefix_sum[i][j][k] = prefix_sum[i - 1][j][k] + prefix_sum[i][j - 1][k] \
                            - prefix_sum[i - 1][j - 1][k] + grid_cnt[i - 1][j - 1][k]

for _ in range(p):
    r1, c1, r2, c2 = map(int, input().split())

    for l in range(3):
        print(prefix_sum[r2][c2][l] - prefix_sum[r2][c1 - 1][l] - \
              prefix_sum[r1 - 1][c2][l] + prefix_sum[r1 - 1][c1 - 1][l], end=' ')
    print()
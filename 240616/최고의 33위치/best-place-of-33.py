n = int(input())
plane = [list(map(int, input().split()))
        for _ in range(n)]

max_coin = 0

for row in range(0, n - 2):
    for col in range(0, n - 2):
        cnt = 0
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                cnt += plane[i][j]
        if cnt > max_coin:
            max_coin = cnt

print(max_coin)
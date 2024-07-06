n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [-1, -1, 1, 1]
dys = [1, -1, -1, 1]


def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)


ans = 0
# 시작점 선정
for i in range(n):
    for j in range(n):
        for p in range(1, n):
            x1, y1 = i + dxs[0] * p, j + dys[0] * p
            if not in_range(x1, y1):
                break

            for q in range(1, n):
                x2, y2 = x1 + dxs[1] * q, y1 + dys[1] * q
                if not in_range(x2, y2):
                    break

                x3, y3 = x2 + dxs[2] * p, y2 + dys[2] * p
                if not in_range(x3, y3):
                    break
                    
                x4, y4 = x3 + dxs[3] * q, y3 + dys[3] * q
                if not in_range(x4, y4):
                    break
                
                # 시작점으로부터 1, 2, 3, 4번 방향 순회가 모두 가능할 경우 값 계산 진행
                tmp = 0
                x, y = i, j
                for _ in range(p):
                    nx, ny = x + dxs[0], y + dys[0]
                    tmp += grid[nx][ny]
                    x, y = nx, ny

                for _ in range(q):
                    nx, ny = x + dxs[1], y + dys[1]
                    tmp += grid[nx][ny]
                    x, y = nx, ny

                for _ in range(p):
                    nx, ny = x + dxs[2], y + dys[2]
                    tmp += grid[nx][ny]
                    x, y = nx, ny

                for _ in range(q):
                    nx, ny = x + dxs[3], y + dys[3]
                    tmp += grid[nx][ny]
                    x, y = nx, ny

                ans = max(ans, tmp)

print(ans)
n = int(input())
x, y = map(lambda x: int(x) - 1, input().split())
grid = [
    list(input())
    for _ in range(n)
]

# 방향: 오른쪽, 아래, 왼쪽, 위
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 초기 방향: 오른쪽
dir_idx = 0

visited = set()
visited.add((x, y, dir_idx))

ans = 0

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)

while True:
    dx, dy = directions[dir_idx]
    nx, ny = x + dx, y + dy

    # 격자 밖으로 나가는 경우 탈출 성공
    if not in_range(nx, ny):
        ans += 1
        break

    # 탈출하지 않았는데, 이미 방문했던 곳이라면 탈출 불가
    if (nx, ny, dir_idx) in visited:
        ans = -1
        break

    # 벽이 있는 경우: 반 시계 방향으로 회전
    if grid[nx][ny] == '#':
        dir_idx = (dir_idx - 1) % 4
    else:
        x, y = nx, ny
        visited.add((x, y, dir_idx))
        ans += 1

        # 오른쪽 벽을 짚고 가기 위한 계산
        right_dir_idx = (dir_idx + 1) % 4
        right_x, right_y = nx + directions[right_dir_idx][0], ny + directions[right_dir_idx][1]

        # 이동할 수 있고 오른쪽에 벽이 있는 경우: 한 칸 이동
        if in_range(right_x, right_y):
            if grid[right_x][right_y] != '#':
                dir_idx = right_dir_idx
                x, y = right_x, right_y
                visited.add((x, y, dir_idx))
                ans += 1

print(ans)
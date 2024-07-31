n, m, r, c = map(int, input().split())
r, c = r - 1, c - 1
directions = list(input().split())
grid = [[0] * n for _ in range(n)]

# 초기 주사위 상태
# 주사위 면 인덱스: [상단, 하단, 전면, 후면, 좌측, 우측]
dice = [1, 6, 2, 5, 4, 3]

# 방향 매핑
# 'L': 왼쪽, 'R': 오른쪽, 'U': 위, 'D': 아래
moves = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

def roll_dice(dice, direction):
    top, bottom, front, back, left, right = dice
    if direction == 'L':
        return [right, left, front, back, top, bottom]
    elif direction == 'R':
        return [left, right, front, back, bottom, top]
    elif direction == 'U':
        return [front, back, bottom, top, left, right]
    elif direction == 'D':
        return [back, front, top, bottom, left, right]

grid[r][c] = dice[1]

# 주사위 굴리기
for direction in directions:
    dx, dy = moves[direction]
    nr, nc = r + dx, c + dy
    
    if 0 <= nr < n and 0 <= nc < n:
        dice = roll_dice(dice, direction)
        grid[nr][nc] = dice[1]
        r, c = nr, nc

print(sum(sum(row) for row in grid))
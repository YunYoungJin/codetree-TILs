n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

bomb_positions = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
total_bomb_cnt = len(bomb_positions)
bomb_types = []
ans = 0

def apply_bomb():
    affected = [[False] * n for _ in range(n)]
    
    for (r, c), bomb_type in zip(bomb_positions, bomb_types):
        if bomb_type == 1:  # Pattern 1
            pattern = [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)]
        elif bomb_type == 2:  # Pattern 2
            pattern = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
        elif bomb_type == 3:  # Pattern 3
            pattern = [(0, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for dr, dc in pattern:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                affected[nr][nc] = True

    return sum(row.count(True) for row in affected)

def select_bomb(cnt):
    global ans
    if cnt == total_bomb_cnt:
        ans = max(ans, apply_bomb())
        return

    for i in range(1, 4):
        bomb_types.append(i)
        select_bomb(cnt + 1)
        bomb_types.pop()

select_bomb(0)

print(ans)
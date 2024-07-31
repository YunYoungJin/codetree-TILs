from collections import deque

n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def bfs(min_val, max_val):
    if not (min_val <= grid[0][0] <= max_val):
        return False
    
    directions = [(0, 1), (1, 0)]
    queue = deque([(0, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == n - 1:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if min_val <= grid[nx][ny] <= max_val:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return False

result = 100

# 최솟값을 고정하고 최댓값을 최소화
for min_val in range(1, 101):
    left, right = min_val, 100
    while left <= right:
        mid = (left + right) // 2
        if bfs(min_val, mid):
            result = min(result, mid - min_val)
            right = mid - 1
        else:
            left = mid + 1

print(result)
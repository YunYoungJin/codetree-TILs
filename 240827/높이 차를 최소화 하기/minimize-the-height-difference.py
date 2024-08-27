from collections import deque

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def is_possible(lower_bound, upper_bound):
    if not (lower_bound <= grid[0][0] <= upper_bound):
        return False

    q = deque()
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            return True

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if lower_bound <= grid[nx][ny] <= upper_bound:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    
    return False

min_value, max_value = min(map(min, grid)), max(map(max, grid))
left, right = 0, max_value - min_value
ans = 500

while left <= right:
    mid = (left + right) // 2
    possible = False

    for min_height in range(min_value, max_value + 1):
        if min_height + mid > max_value:
            break
        if is_possible(min_height, min_height + mid):
            possible = True
            break
    
    if possible:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
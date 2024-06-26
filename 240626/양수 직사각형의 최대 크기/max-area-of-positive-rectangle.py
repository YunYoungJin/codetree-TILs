n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def get_size(x1, y1, x2, y2):
    return (x2 - x1 + 1) * (y2 - y1 + 1)

def check_positive(x1, y1, x2, y2):
    for p in range(x1, x2 + 1):
        for q in range(y1, y2 + 1):
            if grid[p][q] <= 0:
                return False
    return True

max_rect = -1

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                if check_positive(i, j, k, l):
                    max_rect = max(max_rect, get_size(i, j, k, l))

print(max_rect)
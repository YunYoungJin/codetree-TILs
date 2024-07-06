import sys

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def check_not_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
    return x4 < x1 or x2 < x3 or y4 < y1 or y2 < y3

def get_sum(x1, y1, x2, y2):
    tmp_sum = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            tmp_sum += grid[i][j]
    
    return tmp_sum

ans = -sys.maxsize

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                for p in range(n):
                    for q in range(m):
                        for r in range(p, n):
                            for s in range(q, m):
                                if check_not_overlap(i, j, k, l, p, q, r, s):
                                    rect1 = get_sum(i, j, k, l)
                                    rect2 = get_sum(p, q, r, s)
                                    ans = max(ans, rect1 + rect2)

print(ans)
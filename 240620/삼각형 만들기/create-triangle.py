n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def make_triangle(i, j, k):
    s = 0
    tmp = [points[i], points[j], points[k]]
    tmp.sort()
    x1, y1 = tmp[0]
    x2, y2 = tmp[1]
    x3, y3 = tmp[2]

    if x1 == x2 and x2 != x3:
        if (y1 != y2 and y1 == y3) or (y1 != y2 and y2 == y3):
            s = abs((x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3))
    elif x1 != x2 and x2 == x3:
        if (y2 != y3 and y1 == y2) or (y2 != y3 and y1 == y3):
            s = abs((x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3))
    
    return s

ans = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            ans = max(ans, make_triangle(i, j, k))

print(ans)
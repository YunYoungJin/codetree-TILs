n, m, q = map(int, input().split())

building = [
    list(map(int, input().split()))
    for _ in range(n)
]

winds = [
    tuple(map(int, input().split()))
    for _ in range(q)
]

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return (0 <= x and x < n) and (0 <= y and y < m)

def shift(r1, c1, r2, c2):
    tmp = building[r1][c2]

    for c in range(c2, c1, -1):
        building[r1][c] = building[r1][c - 1]

    tmp2 = building[r2][c2]
    for r in range(r2, r1, -1):
        building[r][c2] = building[r - 1][c2]
    building[r1 + 1][c2] = tmp

    tmp = building[r2][c1]
    for c in range(c1, c2 - 1):
        building[r2][c] = building[r2][c + 1]
    building[r2][c2 - 1] = tmp2

    for r in range(r1, r2 - 1):
        building[r][c1] = building[r + 1][c1]
    building[r2 - 1][c1] = tmp

def change(r1, c1, r2, c2):
    tmp_value = [[-1] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            cnt = 1
            tmp_sum = building[i][j]

            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if in_range(nx, ny):
                    cnt += 1
                    tmp_sum += building[nx][ny]

            tmp_value[i - r1][j - c1] = tmp_sum // cnt


    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            building[i][j] = tmp_value[i - r1][j - c1]


for wind in winds:
    r1, c1, r2, c2 = wind
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

    shift(r1, c1, r2, c2)
    change(r1, c1, r2, c2)

for floor in building:
    print(*floor)
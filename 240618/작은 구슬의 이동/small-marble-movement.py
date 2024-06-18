n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

move_dir = mapper[d]

for i in range(t):
    nx, ny = r + dxs[move_dir], c + dys[move_dir]

    if not in_range(nx, ny):
        move_dir = 3 - move_dir
        continue
    
    r, c = nx, ny

print(r, c)
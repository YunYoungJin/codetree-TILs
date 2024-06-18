dx, dy = [1, -1, 0, 0], [0, 0, -1, 1] # E, W, S, N

x, y = 0, 0

n = int(input())

for _ in range(n):
    s = input().split()
    if s[0] == 'E':
        for _ in range(int(s[1])):
            x, y = x + dx[0], y + dy[0]
    elif s[0] == 'W':
        for _ in range(int(s[1])):
            x, y = x + dx[1], y + dy[1]
    elif s[0] == 'S':
        for _ in range(int(s[1])):
            x, y = x + dx[2], y + dy[2]
    else:
        for _ in range(int(s[1])):
            x, y = x + dx[3], y + dy[3]

print(x, y)
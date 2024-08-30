n = int(input())
grid = [
    list(map(int, input()))
    for _ in range(n)
]

def switch(r, c):
    for i in range(r + 1):
        for j in range(c + 1):
            grid[i][j] = 1 - grid[i][j]

ans = 0

for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if grid[i][j] == 1:
            ans += 1
            switch(i, j)

print(ans)
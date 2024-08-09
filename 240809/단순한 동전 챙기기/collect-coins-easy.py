import sys

INT_MAX = sys.maxsize

n = int(input())
grid = [
    list(input())
    for _ in range(n)
]
min_moves = INT_MAX
start = end = None
coins = []
selected = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'E':
            end = (i, j)
        elif grid[i][j].isdigit():
            coins.append((int(grid[i][j]), i, j))

coins.sort()
max_coins = len(coins)

def calc():
    global min_moves
    tmp = 0
    tmp += abs(start[0] - selected[0][1]) + abs(start[1] - selected[0][2])
    tmp += abs(selected[0][1] - selected[1][1]) + abs(selected[0][2] - selected[1][2])
    tmp += abs(selected[1][1] - selected[2][1]) + abs(selected[1][2] - selected[2][2])
    tmp += abs(selected[2][1] - end[0]) + abs(selected[2][2] - end[1])

    min_moves = min(min_moves, tmp)
    return

def choose(idx, cnt):
    if cnt == 3:
        calc()
        return
    
    if idx == max_coins:
        return

    selected.append(coins[idx])
    choose(idx + 1, cnt + 1)
    selected.pop()

    choose(idx + 1, cnt)

choose(0, 0)

print(min_moves if min_moves != INT_MAX else -1)
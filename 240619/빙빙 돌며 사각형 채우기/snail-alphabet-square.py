n, m = map(int, input().split())
answer = [
    [''] * m
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
x, y = 0, 0           # 시작은 (0, 0)
dir_num = 0           # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽

# 처음 시작 위치에 초기값을 적습니다.
alpha = ord('A')
answer[x][y] = chr(alpha)

for i in range(1, n * m):
    # 현재 방향을 기준으로 그 다음 위치 값 갱신
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    # 더 이상 나아갈 수 없다면
    # 시계방향으로 90'를 회전
    if not in_range(nx, ny) or answer[nx][ny] != '':
        dir_num = (dir_num + 1) % 4

    # 그 다음 위치로 이동한 다음 배열에 올바른 값을 채워넣습니다.
    x, y = x + dxs[dir_num], y + dys[dir_num]
    alpha += 1
    if alpha > ord('Z'):
        alpha = ord('A')
    answer[x][y] = chr(alpha)

# 출력:
for i in range(n):
    for j in range(m):
        print(answer[i][j], end = ' ')
    print()
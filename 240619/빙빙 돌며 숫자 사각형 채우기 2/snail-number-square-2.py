n, m = map(int, input().split())
answer = [
    [0] * m
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

dir_num = 0
# 0: 아래쪽, 1: 오른쪽, 2: 위쪽, 3: 왼쪽
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
x, y = 0, 0           # 시작은 (0, 0)

# 처음 시작 위치에 초기값
answer[x][y] = 1

for i in range(2, n * m + 1):
    # 현재 방향을 기준으로 다음 위치 갱신
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    # 더 이상 나아갈 수 없다면
    # 반시계방향으로 90'를 회전
    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    # 그 다음 위치로 이동한 다음 배열에 올바른 값 입력
    x, y = x + dxs[dir_num], y + dys[dir_num]
    answer[x][y] = i

# 출력:
for i in range(n):
    for j in range(m):
        print(answer[i][j], end = ' ')
    print()
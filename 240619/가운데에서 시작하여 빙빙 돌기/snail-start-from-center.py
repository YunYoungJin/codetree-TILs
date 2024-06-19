n = int(input())
answer = [
    [0] * n
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
x, y = n - 1, n - 1   # 거꾸로 채우기 시작하기 위한 위치
dir_num = 2           # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽

# 마지막 위치에 초기값을 적습니다.
answer[x][y] = n ** 2

for i in range(n * n - 1, 0, -1):
    # 현재 방향을 기준으로 그 다음 위치 값 갱신
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    # 더 이상 나아갈 수 없다면
    # 시계방향으로 90'를 회전
    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    # 그 다음 위치로 이동한 다음 배열에 올바른 값을 채워넣습니다.
    x, y = x + dxs[dir_num], y + dys[dir_num]
    answer[x][y] = i

# 출력:
for i in range(n):
    for j in range(n):
        print(answer[i][j], end = ' ')
    print()
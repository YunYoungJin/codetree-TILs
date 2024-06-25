n, m, q = map(int, input().split())
building = [
    list(map(int, input().split()))
    for _ in range(n)
]

winds = [
    input().split()
    for _ in range(q)
]

# row번 행 좌향 shift
def shift_left(row):
    temp = building[row][0]
        
    for i in range(m - 1):
        building[row][i] = building[row][i + 1]
    building[row][m - 1] = temp

# row번 행 우향 shift
def shift_right(row):

    temp = building[row][m - 1]

    for i in range(m - 1, 0, -1):
        building[row][i] = building[row][i - 1]
    building[row][0] = temp


for wind in winds:
    r, d = wind
    r = int(r)
    up_d, down_d = '', ''

    # r번 행 shift
    if d == 'L':
        shift_right(r - 1)
        up_d, down_d = 'R', 'R'
    elif d == 'R':
        shift_left(r - 1)
        up_d, down_d = 'L', 'L'

    # r 기준 위쪽 전파
    for row in range(r - 2, -1, -1):
        propagation = False

        for col in range(m):
            # 같은 열 숫자가 하나라도 같으면
            if building[row + 1][col] == building[row][col]:
                propagation = True
                break
        
        # 전파 중단
        if not propagation:
            break

        if up_d == 'L':
            shift_right(row)
            up_d = 'R'
        else:
            shift_left(row)
            up_d = 'L'


    # r 기준 아래쪽 전파
    for row in range(r, n):
        propagation = False

        for col in range(m):
            if building[row - 1][col] == building[row][col]:
                propagation = True
                break
        
        # 전파 중단
        if not propagation:
            break            

        if down_d == 'L':
            shift_right(row)
            down_d = 'R'
        else:
            shift_left(row)
            down_d = 'L'

for row in building:
    print(*row)
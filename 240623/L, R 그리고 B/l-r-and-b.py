board = [
    list(input())
    for _ in range(10)
]

Lx, Ly, Rx, Ry, Bx, By = 0, 0, 0, 0, 0, 0

for i in range(10):
    for j in range(10):
        if board[i][j] == 'L':
            Lx, Ly = i, j
        elif board[i][j] == 'B':
            Bx, By = i, j
        elif board[i][j] == 'R':
            Rx, Ry = i, j
        

ans = 0
# 행, 열이 모두 다른 위치에 있을 경우
if Lx != Bx and Ly != By:
    ans = abs(Bx - Lx) + abs(By - Ly) - 1
# 행이 같을 경우
elif Lx == Bx:
    # 두 지점 사이에 R이 있다면
    if Lx == Rx and ((Ly < Ry and Ry < By) or (By < Ry and Ry < Ly)):
        ans = abs(By - Ly) + 1
    # 두 지점 사이에 R이 없다면
    else:    
        ans = abs(By - Ly) - 1
# 열이 같을 경우
elif Ly == By:
    # 두 지점 사이에 R이 있다면
    if Ly == Ry and ((Lx < Rx and Rx < Bx) or (Bx < Rx and Rx < Lx)):
        ans = abs(Bx - Lx) + 1
    # 두 지점 사이에 R이 없다면
    else:    
        ans = abs(Bx - Lx) - 1

print(ans)
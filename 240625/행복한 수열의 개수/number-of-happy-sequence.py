n, m = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = 0
for row in board:
    if n == 1:
        ans += 1
        break
    
    cnt = 1
    for i in range(n - 1):
        if row[i] == row[i + 1]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= m:
            ans += 1
            break
    
for j in range(n):
    if n == 1:
        ans += 1
        break
    
    cnt = 1
    for k in range(n - 1):
        if board[k][j] == board[k + 1][j]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= m:
            ans += 1
            break

print(ans)
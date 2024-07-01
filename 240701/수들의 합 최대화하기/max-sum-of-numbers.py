n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 열의 색칠 여부 체크
col = [False] * n
ans = 0

# curr_row 행에서 색칠
def coloring(curr_row, tmp_sum):
    if curr_row == n:
        global ans
        ans = max(ans, tmp_sum)
        return
    
    for j in range(n):
        # 이미 색칠된 열이라면 스킵
        if col[j] != True:
            col[j] = True
            tmp_sum += grid[curr_row][j]
            coloring(curr_row + 1, tmp_sum)
            tmp_sum -= grid[curr_row][j]
            col[j] = False

coloring(0, 0)
print(ans)
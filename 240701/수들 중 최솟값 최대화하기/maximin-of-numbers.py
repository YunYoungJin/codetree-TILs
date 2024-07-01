n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 열의 색칠 여부 체크
col = [False] * n
picked = []
ans = 0

def coloring(row):
    global ans
    
    if row == n:
        tmp_min = 10001
        for i in range(n):
            tmp_min = min(tmp_min, grid[i][picked[i]])

        # 답을 갱신
        ans = max(ans, tmp_min)
        return

    # 현재 행에 색칠할 열을 선택
    for i in range(n):
        if col[i]: 
            continue
        
        col[i] = True
        picked.append(i)

        coloring(row + 1)

        col[i] = False
        picked.pop()


coloring(0)

print(ans)
board = [
    list(input())
    for _ in range(3)
]

ans = 0

lines = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
[(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), ( 1, 2), (2, 2)],
[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]

# 팀 먹을 숫자 2개 
for i in range(1, 10):
    for j in range(i + 1, 10):
        
        # 8개 라인
        for line in lines:
            tmp = [0, 0]
            for x, y in line:
                if board[x][y] == str(i):
                    tmp[0] += 1
                elif board[x][y] == str(j):
                    tmp[1] += 1
            if tmp[0] != 0 and tmp[1] != 0 and sum(tmp) == 3:
                ans += 1
                break
print(ans)
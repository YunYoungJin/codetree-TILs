import sys
n = int(input())
seats = list(input())

ans = 0

max_dist = 0
max_i, max_j = -1, -1
for i in range(n):
    if seats[i] == '1':
        # 인접한 쌍이 있는지 확인
        exist = False
        for j in range(i + 1, n):
            if seats[j] == '1':
                exist = True
                if j - i > max_dist:
                    max_dist = j - i

                    # 이때, 두 좌석의 위치를 기억합니다.
                    max_i, max_j = i, j
                
                # 인접한 쌍을 찾았으므로 빠져나옵니다.
                break
        if exist:
            continue
        else:
            if j - i >= (max_j - max_i) // 2:
                seats[j] = '1'
                break
            else:
                seats[(max_j - max_i) // 2] = '1'
        
# 이제 인접한 쌍들 중 가장 가까운 쌍의 거리 찾기
ans = sys.maxsize
for i in range(n):
    if seats[i] == '1':
        for j in range(i + 1, n):
            if seats[j] == '1':
                ans = min(ans, j - i)
                break

print(ans)
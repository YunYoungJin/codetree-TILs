import sys
n = int(input())
seats = list(input())

tmp_dist = 0
# 0으로 시작할 경우 가상의 거리 
if seats[0] == '0':
    for k in range(1, n):
        if seats[k] == '1':
            tmp_dist = k
            break

# 인접한 쌍이 존재할 때의 최대 거리
max_dist = 0
max_i, max_j = -1, -1
for i in range(n):
    if seats[i] == '1' and i != n - 1:
        # 인접한 쌍이 있는지 확인
        exist = False
        for j in range(i + 1, n):
            if seats[j] == '1':
                exist = True
                # 인접한 쌍의 최대 거리가 갱신 될 때
                if j - i > max_dist:
                    max_dist = j - i
                    # 이때의 두 좌석의 위치를 기억
                    max_i, max_j = i, j
                break
        # 인접한 쌍을 찾았으면 다음 쌍 찾기 진행
        if exist:
            continue
        else:
            if tmp_dist >= n - 1 - i:
                if tmp_dist >= (max_j - max_i) // 2:
                    seats[0] = '1'
                    break
                else:
                    seats[(max_j - max_i) // 2] = '1'
                    break    
            else:
                if n - 1 - i >= (max_j - max_i) // 2:
                    seats[n - 1] = '1'
                    break
                else:
                    seats[(max_j - max_i) // 2] = '1'
                    break
    # 마지막에만 1이 존재 하는 경우라면
    elif seats[i] == '1' and i == n - 1:
        seats[0] = '1'

ans = sys.maxsize
# 이제 인접한 쌍들 중 가장 가까운 쌍의 거리 찾기
for i in range(n):
    if seats[i] == '1':
        for j in range(i + 1, n):
            if seats[j] == '1':
                ans = min(ans, j - i)
                break

print(ans)
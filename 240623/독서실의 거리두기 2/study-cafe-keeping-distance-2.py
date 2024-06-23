import sys
n = int(input())
seats = list(input())

tmp_dist = 0
f_or_b = ''

# 0으로 시작할 경우 가장 가까운 1과의 거리
if seats[0] == '0':
    for k in range(1, n):
        if seats[k] == '1':
            f_dist = k
            tmp_dist = max(tmp_dist, f_dist)
            break

# 0으로 끝나는 경우 가장 가까운 1과의 거리가 tmp_dist보다 크다면 갱신
if seats[n - 1] == '0':
    for k in range(n - 2, -1, -1):
        if seats[k] == '1':
            b_dist = n - 1 - k
            if b_dist > tmp_dist:
                tmp_dist = b_dist
                f_or_b = 'b'
            else:
                f_or_b = 'f'
            break


# 인접한 쌍이 존재할 때의 최대 거리
max_dist = 0
max_i, max_j = -1, -1
for i in range(n):
    if seats[i] == '1':
        # 인접한 쌍이 있는지 확인
        for j in range(i + 1, n):
            if seats[j] == '1':
                # 인접한 쌍의 최대 거리가 갱신 될 때
                if j - i > max_dist:
                    max_dist = j - i
                    # 이때의 두 좌석의 위치를 기억
                    max_i, max_j = i, j
                break

# 인접한 쌍이 존재한다면 거리가 최소 1번은 갱신되니 0은 아니다
if max_dist != 0:
    if tmp_dist >= (max_j - max_i) // 2:
        if f_or_b == 'f':
            seats[0] = '1'
        elif f_or_b == 'b':
            seats[n - 1] = '1'
    else:
        seats[(max_j + max_i) // 2] = '1'
# 인접한 쌍이 하나도 없다면 앞 또는 뒤 중 적절한 곳에 배치
else:
    if f_or_b == 'f':
        seats[0] = '1'
    elif f_or_b == 'b':
        seats[n - 1] = '1'

ans = sys.maxsize
# 이제 인접한 쌍들 중 가장 가까운 쌍의 거리 찾기
for i in range(n):
    if seats[i] == '1':
        for j in range(i + 1, n):
            if seats[j] == '1':
                ans = min(ans, j - i)
                break

print(ans)
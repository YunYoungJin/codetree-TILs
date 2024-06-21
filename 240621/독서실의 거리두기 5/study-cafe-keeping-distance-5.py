n = int(input())
seat = list(map(int, input()))

ans = 0

# 한 명을 추가로 넣을 위치
for i in range(n):
    # 이미 배정된 좌석이면 생략
    if seat[i] == 1:
        continue

    dist = 20
    seat[i] = 1

    for j in range(n):
        for k in range(j + 1, n):
            if seat[j] == 1 and seat[k] == 1:
                dist = min(dist, k - j)
    
    ans = max(ans, dist)

    # 좌석 확인 전 상태로 복구
    seat[i] = 0

print(ans)
n = int(input())
seat = list(map(int, input()))

ans = 0

# 첫 번째 사람을 추가로 넣을 위치
for i in range(n):
    # 두 번째 사람을 추가로 넣을 위치
    for j in range(i + 1, n):
        # 두 자리가 모두 비어 있는 경우만 가능
        if seat[i] == 0 and seat[j] == 0:

            dist = 100
            seat[i], seat[j] = 1, 1

            for k in range(n):
                for l in range(k + 1, n):
                    if seat[k] == 1 and seat[l] == 1:
                        dist = min(dist, l - k)
            
            ans = max(ans, dist)

            # 좌석 확인 전 상태로 복구
            seat[i], seat[j] = 0, 0

print(ans)
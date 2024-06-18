import sys

n = int(input())
pnum_of_room = [int(input()) for _ in range(n)]

min_dist = sys.maxsize

# i번 방에서 출발
for i in range(1, n + 1):
    # 최소거리합 계산
    dist_sum = 0
    # j번 방에 도착
    for j in range(1, n + 1):
        diff = (j - i + n) % n
        dist_sum +=  pnum_of_room[j - 1] * diff
    min_dist = min(min_dist, dist_sum)

print(min_dist)
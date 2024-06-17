n, k, p, T = map(int, input().split())

infect_cnt = [0] * (n + 1) # 감염시킨 횟수
cold = [0] * (n + 1) # 감염 여부
cold[p] = 1
ts = []

for _ in range(T):
    ts.append(list(map(int, input().split())))
ts.sort() # 악수 순서 정렬

for item in ts:
    _, x, y = item
    if (infect_cnt[x] < k and cold[x] == 1) or (infect_cnt[y] < k and cold[y] == 1):
        if cold[x] == 1:
            infect_cnt[x] += 1
        if cold[y] == 1:
            infect_cnt[y] += 1
        cold[x] = 1
        cold[y] = 1

for i in range(1, n + 1):
    print(cold[i], end='')
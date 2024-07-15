n = int(input())
bombs = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

bombs.sort(key=lambda x: -x[0])

max_time = max(bomb[1] for bomb in bombs)
used = [False] * (max_time + 1)  # 특정 시간을 사용했는지 확인하는 리스트
total_score = 0

for score, time_limit in bombs:
    # 가능한 가장 늦은 시간부터 시작해서 시간이 비어 있는지 확인
    for t in range(time_limit, 0, -1):
        if not used[t]:
            used[t] = True
            total_score += score
            break

print(total_score)
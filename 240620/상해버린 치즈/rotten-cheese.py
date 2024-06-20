n, m, d, s = map(int, input().split())

eat_record = [
    tuple(map(int, input().split()))
    for _ in range(d)
]

hurt_record = [
    tuple(map(int, input().split()))
    for _ in range(s)
]

# 사람 별 먹은 치즈
eating_cheese_list = [[] for _ in range(n + 1)]

# 상했을 가능성이 있는 치즈
possible_spoilers = []

# 상했을 가능성이 있는 치즈 찾기
for hurt in hurt_record:
    # 아픈 사람, 아픈 시간
    hp, ht = hurt
    for eat in eat_record:
        # 먹은 사람, 먹은 치즈, 먹은 시간
        ep, em, et = eat
        eating_cheese_list[ep].append(em)
        if hp == ep and et < ht:
            if em not in possible_spoilers:
                possible_spoilers.append(em)

for hurt in hurt_record:
    hp, _ = hurt
    # 상한 가능성이 있는 치즈 중에서
    for possible_spoiler in possible_spoilers[:]:
        # 아픈 사람이 먹지 않은 치즈가 있으면
        if possible_spoiler not in eating_cheese_list[hp]:
            possible_spoilers.remove(possible_spoiler)

# 필요한 약의 개수
ans = 0
for cheese in possible_spoilers:
    # 상했을 가능성이 있는 치즈 먹은 사람 수
    cnt = 0
    for eat in eat_record:
        ep, em, et = eat
        if em == cheese:
            cnt += 1
    ans = max(ans, cnt)

print(ans)
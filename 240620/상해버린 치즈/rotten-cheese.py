'''
10 1 20 5
5 1 9
8 1 3
3 1 2
9 1 1
6 1 4
6 1 9
7 1 1
3 1 1
8 1 10
1 1 2
5 1 7
5 1 5
9 1 4
5 1 6
2 1 1
8 1 1
2 1 1
6 1 2
4 1 3
10 1 3
2 4
7 6
10 9
3 9
1 7
'''
'''
3 2 9 2
2 1 8
1 2 4
1 1 9
3 2 1
3 1 7
3 2 8
3 2 9
1 2 7
1 1 2
1 6
3 6
'''
'''
10 4 20 2
1 2 1 
9 4 7
1 3 5
3 1 4
5 1 7
4 4 9
2 3 6
4 1 9
9 4 8
6 4 5
2 2 4 
8 2 10
6 4 6
9 2 4 
3 2 5 
5 3 3
3 2 7
3 2 6
1 1 7
10 2 8 
5 5
2 7
'''
n, m, d, s = map(int, input().split())

eat_record = [
    tuple(map(int, input().split()))
    for _ in range(d)
]

# n번 사람이 t초에 먹은 순서대로 정렬
eat_record.sort(key = lambda x: (x[0], x[2]))

hurt_record = [
    tuple(map(int, input().split()))
    for _ in range(s)
]

# 1번부터 아픈사람 정렬
hurt_record.sort()

# 상했을 가능성이 있는 치즈 리스트
possible_spoilers = [x for x in range(1, m + 1)]

# 상했을 가능성이 있는 치즈 찾기
for hurt in hurt_record:
    # 아픈 사람, 아픈 시간
    hp, ht = hurt
    # hp번 사람이 아프기 전에 먹은 치즈 리스트
    tmp = []
    for eat in eat_record:
        # 먹은 사람, 먹은 치즈, 먹은 시간
        ep, em, et = eat
        if hp == ep and et < ht:
            if em not in tmp:
                tmp.append(em)

    # 모든 사람이 각각 아프기 전에 공통적으로 먹은 치즈만 선택
    possible_spoilers = list(set(tmp) & set(possible_spoilers))

# 필요한 약의 개수
ans = 0

for cheese in possible_spoilers:
    # 상했을 가능성이 있는 치즈를 먹은 사람 수
    patient_list = []
    for eat in eat_record:
        ep, em, et = eat
        if em == cheese:
            if ep not in patient_list:
                patient_list.append(ep)
    ans = max(ans, len(patient_list))

print(ans)
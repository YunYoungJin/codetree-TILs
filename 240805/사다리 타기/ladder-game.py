n, m = map(int, input().split())
horizontals = [
    tuple(map(int, input().split()))
    for _ in range(m)
]
horizontals.sort(key=lambda x: x[1])

def play_ladder(n, ladder):
    # 각 위치에서의 결과를 계산
    result = list(range(n))
    for a, _ in ladder:
        result[a - 1], result[a] = result[a], result[a - 1]
    return result

initial_result = play_ladder(n, horizontals)

def choose_ladder(index, chosen):
    # 마지막 가로줄 선택여부까지 결정됐으면
    if index == m:
        # 선택된 가로줄들로 만들어진 사다리의 결과를 계산
        chosen_ladders = [horizontals[i] for i in range(m) if chosen[i]]
        # 초기 가로줄로 만들어진 사다리의 결과와 같으면 선택한 사다리 개수 리턴
        if play_ladder(n, chosen_ladders) == initial_result:
            return sum(chosen)
        # 아니면 답이 될 수 없는 값 리턴
        return 16
    
    chosen[index] = True
    include = choose_ladder(index + 1, chosen)
    
    chosen[index] = False
    exclude = choose_ladder(index + 1, chosen)
    
    return min(include, exclude)

chosen = [False] * m
ans = choose_ladder(0, chosen)
print(ans)
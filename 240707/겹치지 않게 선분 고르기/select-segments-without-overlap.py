n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

selected = []

# i 번째 선분
def select(i):
    global ans

    if i == n:
        ans = max(ans, len(selected))
        return

    x1, x2 = segments[i]
    overlay = False
    for x3, x4 in selected:
        if x2 < x3 or x4 < x1:
            continue
        else:
            overlay = True
            break
    
    # 이미 선택한 선분들과 겹치지 않으면 선택해서 체크
    if not overlay:
        selected.append(segments[i])
        select(i + 1)
        selected.remove(segments[i])
    
    # 겹치는 선분이면 다음 선분 체크
    select(i + 1)


ans = 0
select(0)

print(ans)
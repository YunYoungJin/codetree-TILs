n, m = map(int, input().split())
group_A = [
    input()
    for _ in range(n)
]
group_B = [
    input()
    for _ in range(n)
]

ans = 0
selected_idx = []

def check():
    global ans

    s_A = set()
    can_categorize = True

    for nsa in group_A:
        new_comb = ''
        for idx in selected_idx:
            new_comb += nsa[idx]
        s_A.add(new_comb)
    
    for nsb in group_B:
        new_comb = ''
        for idx in selected_idx:
            new_comb += nsb[idx]
        if new_comb in s_A:
            can_categorize = False
            break
    
    if can_categorize:   
        ans += 1


def choose(curr_idx, cnt):
    if cnt == 3:
        check()
        return

    if curr_idx == m:
        return

    selected_idx.append(curr_idx)
    choose(curr_idx + 1, cnt + 1)
    selected_idx.pop()

    choose(curr_idx + 1, cnt)

choose(0, 0)
print(ans)
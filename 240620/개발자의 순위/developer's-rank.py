k, n = map(int, input().split())

plays = [
    list(map(int, input().split()))
    for _ in range(k)
]

ans = 0

# 개발자 별 체크
for i in range(1, n + 1):
    # 항상 낮은 순위일 수 있는 사람
    tmp = []
    # 경기 별 체크
    for idx, play in enumerate(plays):
        # 첫 경기에서 가능한 순서쌍 체크
        if idx == 0:
            for j in range(n):
                # 높은 순위일 때 부터 체크
                if play[j] == i:
                    for k in range(j + 1, n):
                        tmp.append(play[k])
                    break
        # 두 번재 경기부터 불가능하면 제외
        else:
            is_ranked = False
            for j in range(n):
                # i번 개발자보다 높은 순위에 등장하면 제거
                if play[j] == i:
                    is_ranked = True
                if play[j] in tmp and not is_ranked:
                    tmp.remove(play[j])
        if len(tmp) == 0:
            break

    ans += len(tmp)

print(ans)
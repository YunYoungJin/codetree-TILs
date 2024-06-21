n = int(input())
sums = list(map(int, input().split()))
ans = []

# 수열의 첫항으로 가능한 수는 1 ~ (sums[0] - 1)
for i in range(1, sums[0]):
    # 수열 생성이 가능한지
    is_possible = True
    # 임시 수열
    tmp = [i]
    # 숫자가 등장했는지 확인
    exist=[False for _ in range(n + 1)]
    exist[i] = True

    # i로 시작하는 수열을 sum을 기반으로 마지막항까지 확인
    for j in range(n - 1):
        # j + 1 번째 항에 나올 수
        next_num = sums[j] - tmp[j]
        
        # 이미 등장한 수라면 수열 생성 불가
        if exist[next_num] == True:
            is_possible = False
            break
        # 그 수가 등장한 적이 없다면 갱신
        else:
            exist[next_num] = True
            tmp.append(next_num)

    # 수열 생성을 완료 했다면
    if is_possible:
        ans.append(tmp)

ans.sort()
print(*ans[0])
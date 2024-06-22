n, m = map(int, input().split())

arr = list(map(int, input().split()))

# 구간 합들 중 최댓 값이 i라고 가정하고
for i in range(1, 10001):
    # 구간 합
    tmp_sum = 0
    # 칸막이 리스트
    partition = []

    pos = 0
    while pos < n:
        if arr[pos] > i:
            break

        tmp_sum += arr[pos]

        if tmp_sum > i:
            partition.append(pos - 1)
            tmp_sum = arr[pos]
        elif tmp_sum == i and pos != n - 1:
            partition.append(pos)
            tmp_sum = 0
        pos += 1

    if len(partition) <= m - 1 and pos == n:
        print(i)
        break
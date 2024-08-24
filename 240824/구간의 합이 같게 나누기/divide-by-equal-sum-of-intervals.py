n = int(input())
arr = list(map(int, input().split()))

total_sum = sum(arr)
ways = 0

if total_sum % 4 == 0:
    target = total_sum // 4
    current_sum = 0
    count_prefix1 = 0
    count_prefix2 = 0

    for i in range(n - 1):
        current_sum += arr[i]
        
        # 세 번째 구간이 끝날 때까지의 합이 3*target이 되는 경우에 가능한 나누기 방법을 증가
        if current_sum == 3 * target:
            ways += count_prefix2
        
        # 두 번째 구간이 끝날 때까지의 합이 2*target이 되는 경우에 첫 번째 구간의 수를 누적
        if current_sum == 2 * target:
            count_prefix2 += count_prefix1
        
        # 첫 번째 구간의 합이 target이 되는 경우를 카운팅
        if current_sum == target:
            count_prefix1 += 1

print(ways)
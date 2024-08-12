# 변수 선언 및 입력
n, k = tuple(map(int, input().split()))
prefix_sum = [[0] * (n + 1)]

for _ in range(n):
    arr = [0] + list(map(int, input().split()))
    arr_prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        arr_prefix[i] = arr_prefix[i - 1] + arr[i]
    prefix_sum.append(arr_prefix)
    
ans = 0

# 모든 중심에 대해 최댓값을 구하여 비교
for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum_all = 0;
        for r in range(i - k, i + k + 1):
            # r행일때 (j - c ~ j + c)열 까지의 부분합을 더해줍니다.
            c = k - abs(i - r);

            # r행이 범위 안에 있을 경우 부분합을 더해줍니다.
            if 1 <= r and r <= n:
                sum_all += prefix_sum[r][min(j + c, n)] - prefix_sum[r][max(j - c - 1, 0)]
        
        ans = max(ans, sum_all)

print(ans)
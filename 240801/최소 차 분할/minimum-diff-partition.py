n = int(input())
arr = list(map(int, input().split()))

total_sum = sum(arr)
half = total_sum // 2

dp = [False] * (half + 1)
dp[0] = True

for num in arr:
    for j in range(half, num - 1, -1):
        if dp[j - num]:
            dp[j] = True

for i in range(half, 0, -1):
    if dp[i]:
        A_sum = i
        break

B_sum = total_sum - A_sum
print(abs(B_sum - A_sum))
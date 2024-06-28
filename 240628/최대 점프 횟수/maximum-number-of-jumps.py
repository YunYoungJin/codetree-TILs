import sys
INT_MIN = -sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

# 해당 위치까지 올 때의 최대 점프 횟수 
dp = [INT_MIN] * n
dp[0] = 0

for i in range(1, n):
    for j in range(i):
        if dp[j] == INT_MIN:
            break
        
        if j + arr[j] >= i:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
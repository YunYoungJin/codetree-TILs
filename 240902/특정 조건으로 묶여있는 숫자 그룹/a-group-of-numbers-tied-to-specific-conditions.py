import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [
    int(input())
    for _ in range(n)
]
arr.sort()

L = [0] * (n)

# L[i] : i번째 숫자를 시작으로, k이하의 차이를 가지는 숫자 개수
j = 0
for i in range(n):
    while j < n and arr[j] - arr[i] <= k:
        j += 1    
    L[i] = j - i

ans = max(L)

for i in range(n):
    if i + L[i] <= n - 1:
        ans = max(ans, L[i] + max(L[i + L[i]:]))
    else:
        ans = max(ans, L[i])

print(ans)
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [
    int(input())
    for _ in range(n)
]
arr.sort()

L = [0] * (n)
R = [0] * (n)

# L[i] : i번째 숫자를 시작으로, k이하의 차이를 가지는 숫자 개수
j = 0
for i in range(n):
    while j < n and arr[j] - arr[i] <= k:
        j += 1    
    L[i] = j - i

# R[i] : i번째 숫자를 끝으로, k이하의 차이를 가지는 숫자 개수
j = n - 1
for i in range(n - 1, -1, -1):
    while j >= 0 and arr[i] - arr[j] <= k:
        j -= 1
    R[i] = i - j

ans = max(R)

for i in range(n - 1):
    ans = max(ans, R[i] + max(L[i + 1:]))

print(ans)
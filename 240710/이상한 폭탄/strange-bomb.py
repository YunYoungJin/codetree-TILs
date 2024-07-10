n, k = map(int, input().split())
bombs = [
    int(input())
    for _ in range(n)
]

R = [0] * n
last = [-1 for _ in range(1000001)]

for i in range(n):
    R[i] = last[bombs[i]]
    last[bombs[i]] = i

ans = -1
for i in range(n):
    if R[i] != -1 and i - R[i] <= k:
        ans = max(ans, bombs[i])

print(ans)
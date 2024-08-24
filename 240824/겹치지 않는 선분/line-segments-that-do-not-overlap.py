import sys
input = sys.stdin.readline

n = int(input())
segments = []

for _ in range(n):
    x1, x2 = map(int, input().split())
    segments.append((x1, x2))
segments.sort()

L = [0] * n
R = [0] * n

L[0] = segments[0][1]
for i in range(1, n):
    L[i] = max(L[i - 1], segments[i][1])

R[n - 1] = segments[n - 1][1]
for i in range(n - 2, -1, -1):
    R[i] = min(R[i + 1], segments[i][1])

ans = 0
for i in range(n):
    if L[i] == R[i]:
        ans += 1

print(ans)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

if m > n + 1:
    print(0)
    sys.exit(0)

L = [-1] * (m + 2)
R = [-1] * (m + 2)

ai = 1
for bi in range(1, m + 1):
    while ai <= n and A[ai] != B[bi]:
        ai += 1
    L[bi] = ai
    if ai <= n:
        ai += 1

ai = n
for bi in range(m, 0, -1):
    while ai >= 1 and A[ai] != B[bi]:
        ai -= 1
    R[bi] = ai
    if ai >= 1:
        ai -= 1

R[m + 1] = n + 1

ans = 0
for k in range(1, m + 1):
    if L[k - 1] < R[k + 1]:
        ans += 1

print(ans)
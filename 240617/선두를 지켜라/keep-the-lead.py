n, m = map(int, input().split())

A = [0]
B = [0]

first = None
cnt = 0

for _ in range(n):
    v, t = map(int, input().split())
    for i in range(1, t + 1):
        A.append(A[-1] + v)
for _ in range(m):
    v, t = map(int, input().split())
    for i in range(1, t + 1):
        B.append(B[-1] + v)

for i in range(1, len(A)):
    if A[i] > B[i] and first != 'A':
        if first != None:
            cnt += 1
        first = 'A'
    elif A[i] < B[i] and first != 'B':
        if first != None:
            cnt += 1
        first = 'B'

print(cnt)
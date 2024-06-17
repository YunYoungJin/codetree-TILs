n, m = map(int, input().split())

A = [0]
B = [0]
same_pos = True
cnt = 0

for _ in range(n):
    dist, lr = input().split()
    if lr == 'L':
        for _ in range(int(dist)):
            A.append(A[-1] - 1)
    else:
        for _ in range(int(dist)):
            A.append(A[-1] + 1)

for _ in range(m):
    dist, lr = input().split()
    if lr == 'L':
        for _ in range(int(dist)):
            B.append(B[-1] - 1)
    else:
        for _ in range(int(dist)):
            B.append(B[-1] + 1)

if len(A) > len(B):
    for i in range(1, len(B)):
        if A[i] == B[i]:
            if not same_pos:
                cnt += 1
                same_pos = True
        else:
            same_pos = False
    for j in range(i + 1, len(A)):
        if A[j] == B[i]:
            if not same_pos:
                cnt += 1
                same_pos = True
        else:
            same_pos = False
else:
    for i in range(1, len(A)):
        if A[i] == B[i]:
            if not same_pos:
                cnt += 1
                same_pos = True
        else:
            same_pos = False
    for j in range(i + 1, len(B)):
        if A[i] == B[j]:
            if not same_pos:
                cnt += 1
                same_pos = True
        else:
            same_pos = False

print(cnt)
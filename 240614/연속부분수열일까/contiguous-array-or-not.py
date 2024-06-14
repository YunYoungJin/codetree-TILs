n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

satisfied = False
for idx, value in enumerate(A):
    if value == B[0]:
        start = idx
        end = start + n2
        if end <= n1 and B == A[start:end]:
            satisfied = True                
if satisfied:
    print("Yes")
else:
    print("No")
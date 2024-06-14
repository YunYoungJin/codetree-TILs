n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if B[0] in A:
    start = A.index(B[0])
    end = start + len(B)
    if B == A[start:end]:
        print("Yes")
    else:
        print("No")
else:
    print("No")
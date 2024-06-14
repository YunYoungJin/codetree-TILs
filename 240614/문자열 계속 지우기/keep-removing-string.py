A = input()
B = input()

if B not in A:
    print(A)
else:
    while B in A:
        start = A.index(B)
        end = start + len(B)
        A = A[:start] + A[end:]
    print(A)
A, B = input().split()

idx = 0
for c in A:
    idx += 1
    if not c.isdigit():
        A = A[:idx - 1]
        break

idx = 0
for c in B:
    idx += 1
    if not c.isdigit():
        B = B[:idx - 1]
        break
print(int(A) + int(B))
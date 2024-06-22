n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dist = 0
for i in range(n - 1):
    dist += A[i] - B[i]
    A[i + 1] += A[i] - B[i]

print(dist)
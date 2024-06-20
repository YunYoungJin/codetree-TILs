n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

center = 1000000
check = [0] * n

for i in range(n):
    for j in range(i + 1, n):
        x1, x2 = segments[i]
        x3, x4 = segments[j]

        if (x1 < x3 and x4 < x2) or (x3 < x1 and x2 < x4):
            check[i] += 1
            check[j] += 1

print(check.count(0))
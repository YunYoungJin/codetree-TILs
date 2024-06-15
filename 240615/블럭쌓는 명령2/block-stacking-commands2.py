n, k = map(int, input().split())
block = [0] * n

for _ in range(k):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        block[i - 1] += 1
print(max(block))
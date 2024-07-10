n, q = map(int, input().split())

arr = [
    int(input())
    for _ in range(n)
]

prefix_sum = [[0, 0, 0] for _ in range(n + 1)]

for i in range(1, n + 1):
    for k in range(1, 4):
        if k == arr[i - 1]:
            prefix_sum[i][k - 1] = prefix_sum[i - 1][k - 1] + 1
        else:
            prefix_sum[i][k - 1] = prefix_sum[i - 1][k - 1]

for _ in range(q):
    a, b = map(int, input().split())
    for k in range(3):
        print(prefix_sum[b][k] - prefix_sum[a - 1][k], end=' ')
    print()
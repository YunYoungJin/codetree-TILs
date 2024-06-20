n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = 0
for i in range(n):
    count = [0] * 1001
    for j in range(n):
        if j == i:
            continue

        x1, x2 = segments[j]
        for k in range(x1, x2):
            count[k] = 1

    max_cnt = sum(count)
    ans = max(ans, max_cnt)

print(ans)
n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]


def get_max_overlapped_cnt(i1, i2, i3):
    count = [0] * 101
    for i in range(n):
        if i in [i1, i2, i3]: 
            continue

        x1, x2 = segments[i]
        for j in range(x1, x2 + 1):
            count[j] += 1

    return max(count)


ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            max_cnt = get_max_overlapped_cnt(i, j, k)
            if max_cnt == 1:
                ans += 1

print(ans)
n = int(input())

nums = [
    list(map(int, input().split()))
    for _ in range(2)
]

ans = []

for num in nums:
    a, b, c = num

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if (abs(a-i) <= 2 or abs(a-i) >= n - 2) and \
                (abs(b-j) <= 2 or abs(b-j) >= n - 2) and \
                (abs(c-k) <= 2 or abs(c-k) >= n - 2):
                    comb = [i, j, k]
                    if comb not in ans:
                        ans.append(comb)

print(len(ans))
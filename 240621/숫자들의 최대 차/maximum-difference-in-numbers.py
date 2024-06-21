n, k = map(int, input().split())
arr = [
    int(input())
    for _ in range(n)
]

ans = 0


for i in range(1, 10001 - k):
    cnt = 0
    for num in arr:
        if i <= num and num <= i + k:
            cnt += 1
    ans = max(ans, cnt)

print(ans)
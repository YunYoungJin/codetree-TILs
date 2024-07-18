n, k, b = map(int, input().split())
checked = [1] * (n + 1)
checked[0] = 0

for _ in range(b):
    num = int(input())
    checked[num] = 0

prefix_cnt = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_cnt[i] = prefix_cnt[i - 1] + checked[i]

ans = 0
for i in range(1, n - k + 2):
    exist_cnt = prefix_cnt[i + k - 1] - prefix_cnt[i - 1]
    ans = max(ans, exist_cnt)

print(k - ans)
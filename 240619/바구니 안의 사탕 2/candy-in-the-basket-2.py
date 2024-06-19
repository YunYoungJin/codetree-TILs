n, k = map(int, input().split())

line = [0] * 101
for _ in range(n):
    candy, pos = map(int, input().split())
    line[pos] += candy

max_cnt = 0

if k > 50:
    max_cnt = sum(line)

for i in range(k, 101 - k):
    cnt = 0
    for j in range(i - k, i + k +1):
        cnt += line[j]
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
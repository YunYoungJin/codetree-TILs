m1, d1, m2, d2 = map(int, input().split())
A = input()

month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date1 = d1
date2 = d2

for i in range(m1 - 1):
    date1 += month[i]

for j in range(m2 - 1):
    date2 += month[j]

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
cnt = [0] * 7

idx = 0
for _ in range(date2 - date1 + 1):
    cnt[idx] += 1
    idx = (idx + 1) % 7

print(cnt[days.index(A)])
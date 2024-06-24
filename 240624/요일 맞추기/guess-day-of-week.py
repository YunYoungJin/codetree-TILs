m1, d1, m2, d2 = map(int, input().split())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date1 = d1
date2 = d2

for i in range(m1 - 1):
    date1 += month[i]

for j in range(m2 - 1):
    date2 += month[j]

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

if date2 > date1:
    print(days[(date2 - date1) % 7])
else:
    date2 += 7
    print(days[(date2 - date1) % 7])
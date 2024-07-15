n = int(input())
meetings = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

meetings.sort(key=lambda x: x[1])
last = 0
select = 0

for s, e in meetings:
    if s >= last:
        select += 1
        last = e

print(n - select)
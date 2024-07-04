n = int(input())
infos = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

infos.sort(key=lambda x: x[1])

ans = 0

curr_meet = -1

for s, e in infos:
    if s >= curr_meet:
        ans += 1
        curr_meet = e

print(ans)
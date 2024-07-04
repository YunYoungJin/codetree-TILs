n, m = map(int, input().split())

jewels = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

jewels.sort(key=lambda x: -(x[1]/x[0]))

ans = 0
bag = 0
for w, v in jewels:
    if bag + w <= m:
        bag += w
        ans += v
    else:
        ans += v/w * (m - bag)
        break

print(f"{ans:.3f}")
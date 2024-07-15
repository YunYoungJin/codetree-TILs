n = int(input())
bombs = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

bombs.sort(key=lambda x: (x[1], -x[0]))

last_e = 0
ans = 0

for score, t in bombs:
    if last_e < t:
        ans += score
        last_e = t

print(ans)
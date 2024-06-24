n = int(input())

blocks = [
    int(input())
    for _ in range(n)
]

goal = sum(blocks) // len(blocks)

ans = 0
for block in blocks:
    if block < goal:
        ans += goal - block

print(ans)
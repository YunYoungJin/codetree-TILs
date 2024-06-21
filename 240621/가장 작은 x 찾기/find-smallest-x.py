n = int(input())

ans = 10000

infos = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

start = (infos[0][0] // 2) + 1
end = (infos[-1][1] // (2 ** n)) + 1

for x in range(start, end):
    satisfied = True
    num = x
    for a, b in infos:
        num *= 2
        if a <= num and num <= b:
            continue
        
        satisfied = False
        break
    if satisfied:
        ans = min(ans, x)
        break

print(ans)
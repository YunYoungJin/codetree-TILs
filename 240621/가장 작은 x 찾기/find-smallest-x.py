n = int(input())

ans = 10000

infos = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# x가 10이면 2를 10번 곱했을 때 10000보다 크다
for x in range(1, 10):
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

print(x)
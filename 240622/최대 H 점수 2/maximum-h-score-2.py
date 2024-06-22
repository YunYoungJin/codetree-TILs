n, l = map(int, input().split())
arr = list(map(int, input().split()))

for h in range(100, 0, -1):
    already = 0
    possible = 0

    for num in arr:
        if num >= h:
            already += 1
        elif num == h - 1:
            possible += 1
    
    if min(possible, l) + already >= h:
        print(h)
        break
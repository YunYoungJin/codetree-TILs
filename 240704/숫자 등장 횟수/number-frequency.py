n, m = map(int, input().split())
arr = list(map(int, input().split()))
targets = list(map(int, input().split()))

d = dict()

for num in arr:
    if num not in d:
        d[num] = 1
    else:
        d[num] += 1

for target in targets:
    if target in d:
        print(d[target], end=' ')
    else:
        print(0, end=' ')
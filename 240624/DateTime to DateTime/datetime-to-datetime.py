a, b, c = map(int, input().split())

pivot = (10 * 24 + 11) * 60 + 11
target = ((a - 1) * 24 + b) * 60 + c

if target - pivot < 0:
    print(-1)
else:
    print(target - pivot)
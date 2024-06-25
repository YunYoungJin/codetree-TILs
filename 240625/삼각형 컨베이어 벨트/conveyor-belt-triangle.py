from collections import deque

n, t = map(int, input().split())
belts = deque()

for _ in range(3):
    belts.extend(list(map(int, input().split())))

for _ in range(t):
    belts.rotate(1)

for i in range(len(belts)):
    print(belts[i], end=' ')
    if i % n == n - 1:
        print()
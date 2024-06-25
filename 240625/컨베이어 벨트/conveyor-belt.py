from collections import deque

n, t = map(int, input().split())
belts = deque(list(map(int, input().split())) + list(map(int, input().split())))

for _ in range(t):
    belts.rotate(1)

for i in range(len(belts)):
    print(belts[i], end=' ')
    if i % n == n - 1:
        print()
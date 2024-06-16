from collections import deque
n, k = map(int, input().split())
q = deque(i for i in range(1, n + 1))
while len(q) != 0:
    for i in range(1, k):
        q.append(q.popleft())
    print(q.popleft(), end=' ')
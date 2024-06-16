n, k = map(int, input().split())
q = [i for i in range(1, n + 1)]
while len(q) != 0:
    for i in range(1, k):
        q.append(q[0])
        del q[0]
    print(q[0], end=' ')
    del q[0]
n, m = map(int, input().split())
a, b = map(int, input().split())
uf = list(range(n + 1))

edges = [
    tuple(map(int, input().split()))
    for _ in range(m)
]
edges.sort(key=lambda x: -x[2])

def union(x, y):
    X = find(x)
    Y = find(y)

    uf[X] = Y


def find(x):
    if uf[x] != x:
        uf[x] = find(uf[x])

    return uf[x]


ans = 0
for p, q, s in edges:
    union(p, q)

    if find(a) == find(b):
        ans = s
        break

print(ans)
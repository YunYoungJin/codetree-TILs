n = int(input())
parent = list(range(n + 1))

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:
        if rootX < rootY:
            parent[rootY] = rootX
        else:
            parent[rootX] = rootY


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


for _ in range(n - 2):
    a, b = map(int, input().split())
    union(a, b)


components = list(set(find(i) for i in range(1, n + 1)))
components.sort()

print(*components)
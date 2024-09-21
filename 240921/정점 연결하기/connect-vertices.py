n = int(input())
parent = list(range(n + 1))
rank = [0] * (n + 1)

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    elif rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    else:
        parent[rootY] = rootX
        rank[rootX] += 1


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


for _ in range(n - 2):
    a, b = map(int, input().split())
    union(a, b)


components = set(parent[1:])
components = list(components)

comp1 = min(components[0], components[1])
comp2 = max(components[0], components[1])

# 두 대표 정점을 연결하는 간선 출력
print(comp1, comp2)
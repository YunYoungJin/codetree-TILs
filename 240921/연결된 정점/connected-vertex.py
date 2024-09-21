n, m = map(int, input().split())
uf = list(range(n + 1))
size = [1] * (n + 1)

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:
        # 항상 작은 트리를 큰 트리에 합친다.
        if size[rootX] < size[rootY]:
            rootX, rootY = rootY, rootX
        uf[rootY] = rootX
        size[rootX] += size[rootY]


def get_size(x):
    return size[find(x)]


def find(x):
    if uf[x] != x:
        uf[x] = find(uf[x])

    return uf[x]


for _ in range(m):
    command = input().split()

    if command[0] == 'x':
        union(int(command[1]), int(command[2]))
    elif command[0] == 'y':
        a = int(command[1])
        print(get_size(a))
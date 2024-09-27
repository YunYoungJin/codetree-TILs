n = int(input())
uf = list(range(100001))
size = [1] * (100001)

def union(x, y):
    X = find(x)
    Y = find(y)

    if size[X] < size[Y]:
        uf[X] = Y
        size[Y] += size[X]
        size[X] = size[Y]
    else:
        uf[Y] = X
        size[X] += size[Y]
        size[Y] = size[X]

    
def find(x):
    if uf[x] != x:
        uf[x] = find(uf[x])
    
    return uf[x]

for _ in range(n):
    a, b = map(int, input().split())
    union(a, b)
    
    print(max(size[find(a)], size[find(b)]))
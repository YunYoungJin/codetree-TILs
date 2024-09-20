n, m = map(int, input().split())
edges = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

uf = list(range(n + 1))

def union(x, y):
    X = find(x)
    Y = find(y)

    if X == Y:
        return False
    else:
        uf[X] = Y
        return True

def find(x):
    if uf[x] != x:
        uf[x] = find(uf[x])

    return uf[x]

for i, (u, v) in enumerate(edges):
    if not union(u, v):
        print(i + 1)  # 사이클이 처음 발생한 간선 번호 출력
        break
else:
    print("happy")  # 모든 간선을 추가해도 사이클이 없는 경우
n, m, k = map(int, input().split())
uf = list(range(n + 1))

def union(x, y):
    X = find(x)
    Y = find(y)
    uf[X] = Y

def find(x):
    if uf[x] != x:
        uf[x] = find(uf[x])
    return uf[x]

# 간선 정보를 통해 그래프 연결 (유니온-파인드 적용)
for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)

orders = list(map(int, input().split()))

# 주어진 순서대로 이동이 가능한지 체크
is_possible = True
for i in range(1, k):
    if find(orders[i - 1]) != find(orders[i]):
        is_possible = False
        break

print(1 if is_possible else 0)
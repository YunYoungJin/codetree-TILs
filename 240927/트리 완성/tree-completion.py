n, m = map(int, input().split())
uf = list(range(n + 1))
ans = 0

def union(x, y):
    global ans

    X = find(x)
    Y = find(y)

    # 사이클이 발생하면 간선을 끊는다
    if X == Y:
        ans += 1
    else:
        uf[X] = Y


def find(x):
    if uf[x] != x:
        uf[x] = find(uf[x])

    return uf[x]


for _ in range(m):
    a, b = tuple(map(int, input().split()))
    union(a, b)

# 컴포넌트가 여러개인 경우, 연결 필요
components = set(find(i) for i in range(1, n + 1))
ans += len(components) - 1

print(ans)
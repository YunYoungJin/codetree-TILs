n = int(input())

infos = [
    tuple(input().split())
    for _ in range(n)
]

infos.sort(key = lambda x : int(x[1]))

for name, h, w in infos:
    print(f"{name} {h} {w}")
n, k = map(int, input().split())
infos = [
    tuple(map(int, input().split()))
    for _ in range(k)
]

seat = [i for i in range(n + 1)]
seat_check= [
    set([i])
    for i in range(n + 1)
]

for _ in range(3):
    for a, b in infos:
        seat_check[seat[a]].add(b)
        seat_check[seat[b]].add(a)
        seat[a], seat[b] = seat[b], seat[a]

for i in range(1, n + 1):
    print(len(seat_check[i]))
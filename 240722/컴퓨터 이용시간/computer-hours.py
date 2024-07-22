import heapq

n = int(input())
times = []

for i in range(n):
    p, q = map(int, input().split())
    times.append((p, 1, i))
    times.append((q, -1, i))

times.sort()
available_coms = []
used_coms = {}
coms = [0] * n


for t, v, p in times:
    if v == 1:
        if available_coms:
            comp = heapq.heappop(available_coms)
        else:
            comp = len(used_coms)

        used_coms[p] = comp
        coms[p] = comp + 1
    
    else:
        comp = used_coms.pop(p)
        heapq.heappush(available_coms, comp)

print(*coms)
import heapq

n = int(input())
times = []

for i in range(n):
    p, q = map(int, input().split())
    times.append((p, 1, i))
    times.append((q, -1, i))

times.sort(key=lambda x: (x[0], -x[1]))
available_rooms = []
used_rooms = {}

ans = set()

for t, v, p in times:
    if v == 1:
        if available_rooms:
            room = heapq.heappop(available_rooms)
        else:
            room = len(used_rooms)

        used_rooms[p] = room
        ans.add(room + 1)
    
    else:
        room = used_rooms.pop(p)
        heapq.heappush(available_rooms, room)

print(len(ans))
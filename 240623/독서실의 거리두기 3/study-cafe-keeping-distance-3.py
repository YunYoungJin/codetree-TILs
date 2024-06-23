n = int(input())
seats = list(input())

occupied = []
for idx, seat in enumerate(seats):
    if seat == '1':
        occupied.append(idx)

left, right, max_dist = -1, -1, -1
for i in range(len(occupied) - 1):
    dist = occupied[i + 1] - occupied[i]
    if dist > max_dist:
        max_dist = dist
        left, right = occupied[i + 1], occupied[i]

seats[(left + right) // 2] = '1'
occupied.append((left + right) // 2)
occupied.sort()

ans = 1001
for i in range(len(occupied) - 1):
    dist = occupied[i + 1] - occupied[i]
    ans = min(ans, dist)

print(ans)
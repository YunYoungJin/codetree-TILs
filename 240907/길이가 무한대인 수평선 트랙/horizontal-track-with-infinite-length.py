import sys
input = sys.stdin.readline

n, t = map(int, input().split())
people = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

arrival_positions = [x + v * t for x, v in people]
pos_set = set(arrival_positions)

for i in range(len(arrival_positions) - 1, 0, -1):
    if arrival_positions[i - 1] > arrival_positions[i]:
        pos_set.remove(arrival_positions[i - 1])
        arrival_positions[i - 1] = arrival_positions[i]

print(len(pos_set))
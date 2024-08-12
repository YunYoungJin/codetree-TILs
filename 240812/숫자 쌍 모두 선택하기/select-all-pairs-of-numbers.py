n = int(input())
meetings = []

for _ in range(n):
    a, b = map(int, input().split())
    meetings.append((a, 1))
    meetings.append((b, -1))

meetings.sort()

current_rooms = 0
max_rooms = 0

for meeting, v in meetings:
    if v == 1:
        current_rooms += 1
        max_rooms = max(max_rooms, current_rooms)
    else:
        current_rooms -= 1

print(max_rooms)
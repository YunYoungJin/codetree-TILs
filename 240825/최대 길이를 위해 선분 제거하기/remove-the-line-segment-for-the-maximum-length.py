n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

events = []
for x1, x2 in segments:
    events.append((x1, 1))
    events.append((x2, -1))
events.sort()

total_length = 0
curr_cnt = 0
prev_x = None
single_cover_length = [0] * n


for x, v in events:
    if prev_x is not None and curr_cnt > 0:
        total_length += x - prev_x
    
    if curr_cnt == 1:
        for i in range(n):
            if prev_x >= segments[i][0] and x <= segments[i][1]:
                single_cover_length[i] += x - prev_x
                break
    
    curr_cnt += v
    prev_x = x

ans = 0
for i in range(n):
    length = total_length - single_cover_length[i]
    ans = max(ans, length)

print(ans)
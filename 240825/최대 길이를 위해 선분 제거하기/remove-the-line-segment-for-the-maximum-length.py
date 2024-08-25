n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

events = []
for i, (x1, x2) in enumerate(segments):
    events.append((x1, 1, i))
    events.append((x2, -1, i))
events.sort()

total_length = 0
curr_cnt = 0
prev_x = None
single_cover_length = [0] * n


for x, v, i in events:
    if prev_x is not None and curr_cnt > 0:
        total_length += x - prev_x
    
    if curr_cnt == 1:
        single_cover_length[last_segment] += x - prev_x

    if v == 1:
        last_segment = i    
    curr_cnt += v
    prev_x = x


print(total_length - min(single_cover_length))
import heapq

n = int(input())
segments = []

for i in range(1, n + 1):
    y, x1, x2 = map(int, input().split())
    segments.append((x1, 1, y, i))
    segments.append((x2, -1, y, i))

segments.sort()

active_colors = set()
visible_colors = []
answer = 0
check = [False] * (n + 1)

for x, t, y, color in segments:
    if t == 1:  # 선분 시작
        if not active_colors or (visible_colors[0][0] > y):
            answer += 1
            check[color] = True
        heapq.heappush(visible_colors, (y, color))
        active_colors.add(color)    
    else:
        active_colors.remove(color)
        if visible_colors[0][1] == color:
            heapq.heappop(visible_colors)
            while visible_colors and visible_colors[0][1] not in active_colors:
                heapq.heappop(visible_colors)
            if visible_colors and not check[visible_colors[0][1]]:
                answer += 1
                check[visible_colors[0][1]] = True

print(answer)
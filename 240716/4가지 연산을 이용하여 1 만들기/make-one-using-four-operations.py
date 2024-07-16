from collections import deque

n = int(input())
q = deque([(n, 0)])

visited = set()
visited.add(n)
ans = 0

while q:
    current, step = q.popleft()

    if current == 1:
        ans = step
        break
    
    next_steps = [current + 1, current - 1]
    if current % 2 == 0:
        next_steps.append(current // 2)
    if current % 3 == 0:
        next_steps.append(current // 3)

    for next_step in next_steps:
        if next_step not in visited and next_step > 0:
            visited.add(next_step)
            q.append((next_step, step + 1))

print(ans)
from collections import deque

n, g = map(int, input().split())
groups = []
invited = deque([1])

for _ in range(g):
    group = list(map(int, input().split()))
    groups.append(set(group[1:]))

ans = 0
pivot = 0
while invited:
    check = invited.popleft()
    ans += 1
    filtered_groups = []

    for group in groups:
        pivot += 1
        if check in group:
            group.remove(check)

        if len(group) == 1:
            invited.append(group.pop())
        
        if group:
            filtered_groups.append(group)
    
    groups = filtered_groups


print(ans)
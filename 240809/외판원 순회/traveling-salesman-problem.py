import sys

INT_MAX = sys.maxsize

n = int(input())
costs = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = INT_MAX
visited = [False] * n

def track(curr_ver, cnt, cost_sum):
    global ans

    if cnt == n:
        if costs[curr_ver][0] > 0:
            ans = min(ans, cost_sum + costs[curr_ver][0])
        return
    
    for next_ver in range(1, n):
        if not visited[next_ver] and costs[curr_ver][next_ver] > 0:
            visited[next_ver] = True
            track(next_ver, cnt + 1, cost_sum + costs[curr_ver][next_ver])
            visited[next_ver] = False

visited[0] = True
track(0, 1, 0)
print(ans)
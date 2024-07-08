import sys

n, m = map(int, input().split())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

selected = []
ans = sys.maxsize

def calc():
    global ans

    dist = 0
    for i in range(m):
        for j in range(i + 1, m):
            x1, y1 = selected[i]
            x2, y2 = selected[j]
            dist = max(dist, (x1 - x2) ** 2 + (y1 - y2) ** 2)
    ans = min(ans, dist)

def choose(curr_idx, cnt):
    if cnt == m:
        calc()
        return
    
    if curr_idx == n:
        return

    # curr_idx에 해당하는 점을 선택했을 때의 경우를 탐색
    selected.append(points[curr_idx])
    choose(curr_idx + 1, cnt + 1)
    selected.pop()

    # curr_idx에 해당하는 점을 선택하지 않았을 때의 경우를 탐색
    choose(curr_idx + 1, cnt)


choose(0, 0)
print(ans)
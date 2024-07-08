import sys

n = int(input())
arr = list(map(int, input().split()))

ans = sys.maxsize

def find_min_jump(idx, cnt):
    global ans
    
    if idx == n - 1:
        ans = min(ans, cnt)
        return

    if idx >= n:
        return

    available_jump_cnt = arr[idx]
    for i in range(1, available_jump_cnt + 1):
        next_idx = idx + i
        find_min_jump(next_idx, cnt + 1)


find_min_jump(0, 0)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
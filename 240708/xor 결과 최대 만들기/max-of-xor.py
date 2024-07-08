import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = -sys.maxsize

tmp = []

def select_num(idx, cnt):
    global ans

    if idx == n:
        if cnt == m:
            res = tmp[0]
            for idx in range(1, m):
                res = res ^ tmp[idx]
            ans = max(ans, res)
            return
        return

    for i in range(idx, n):
        tmp.append(arr[i])
        select_num(i + 1, cnt + 1)
        tmp.pop()

select_num(0, 0)

print(ans)
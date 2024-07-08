import sys

n = int(input())
arr = list(map(int, input().split()))
sum_of_all = sum(arr)

selected = []
ans = sys.maxsize

def calc():
    global ans
    sum_of_selected  = sum(selected)
    sum_of_unselected = sum_of_all - sum_of_selected
    diff = abs(sum_of_selected - sum_of_unselected)
    ans = min(ans, diff)


def choose(curr_idx, cnt):
    if cnt == n:
        calc()
        return
    
    if curr_idx == 2* n:
        return

    # curr_idx에 해당하는 점을 선택했을 때의 경우를 탐색
    selected.append(arr[curr_idx])
    choose(curr_idx + 1, cnt + 1)
    selected.pop()

    # curr_idx에 해당하는 점을 선택하지 않았을 때의 경우를 탐색
    choose(curr_idx + 1, cnt)


choose(0, 0)
print(ans)
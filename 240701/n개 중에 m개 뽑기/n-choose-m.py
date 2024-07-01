n, m = map(int, input().split())

tmp = []

def Print():
    print(*tmp)
    return

# 현재까지 고른 수 중 가장 큰 수와 개수를 인자로
def select_num(num, cnt):
    if cnt == m:
        Print()
        return
    
    for i in range(num + 1, n + 1):
        if i not in tmp:
            tmp.append(i)
            select_num(i, cnt + 1)
            tmp.pop()

select_num(0, 0)
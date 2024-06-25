k, n = map(int, input().split())

answer = []

def Print():
    print(*answer)    
    return

def select_num(curr_pos):
    if curr_pos == n + 1:
        Print()
        return

    for i in range(1, k + 1):
        answer.append(i)
        select_num(curr_pos + 1)
        answer.pop()

select_num(1)
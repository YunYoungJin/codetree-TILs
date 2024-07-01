n = int(input())

tmp = []

def Print():
    print(*tmp)
    return

def make_permu(curr_pos):
    if curr_pos == n + 1:
        Print()
        return
    
    for i in range(1, n + 1):
        if i not in tmp:
            tmp.append(i)
            make_permu(curr_pos + 1)
            tmp.pop()

make_permu(1)
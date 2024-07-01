n = int(input())

tmp = []

def Print():
    print(*tmp)
    return

def get_reverse_permutation(curr_pos):
    if curr_pos == n + 1:
        Print()
        return
    
    for i in range(n, 0, -1):
        if i not in tmp:
            tmp.append(i)
            get_reverse_permutation(curr_pos + 1)
            tmp.pop()

get_reverse_permutation(1)
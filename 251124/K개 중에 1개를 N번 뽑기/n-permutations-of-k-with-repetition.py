K, N = map(int, input().split())

# Please write your code here.
ans = []

def print_ans():
    for num in ans:
        print(num, end=' ')
    print()

# cur_num 현재까지 고른 숫자 개수
def select(cur_num):
    if cur_num == N:
        print_ans()
        return
    
    for i in range(1, K+1):
        ans.append(i)
        select(cur_num+1)
        ans.pop()

select(0)
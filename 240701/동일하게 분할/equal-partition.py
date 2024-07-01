import sys

n = int(input())
arr = list(map(int, input().split()))

if sum(arr) % 2 == 1:
    print("No")
    sys.exit()

target = sum(arr) // 2
picked = []

# 현재까지 고른 수의 인덱스 리스트와 부분합 인자로
def select_num(picked, sub_sum):
    if sub_sum == target and len(picked) < n:
        print("Yes")
        sys.exit()
    
    for i in range(n):
        if i not in picked:
            if sub_sum + arr[i] <= target:
                picked.append(i)
                select_num(picked, sub_sum + arr[i])
                picked.pop()

select_num(picked, 0)
print("No")
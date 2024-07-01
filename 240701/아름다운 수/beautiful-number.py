n = int(input())

arr = []
ans = 0

def is_beauti_num(arr):
    i = 0
    while i < n:
        num = arr[i]
        cnt = 1

        while i < n - 1:
            if arr[i + 1] != num:
                break
            cnt += 1
            i += 1
        
        if cnt % num != 0:
            return False

        i += 1

    return True

def select_num(curr_pos):
    if curr_pos == n + 1:
        if is_beauti_num(arr):
            global ans
            ans += 1
        return

    for num in range(1, 5):
        arr.append(num)
        select_num(curr_pos + 1)
        arr.pop()

select_num(1)
print(ans)
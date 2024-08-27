A = input()
B = input()
remove_order = list(map(lambda x: int(x) - 1, input().split()))

def check_substring(mid):
    n = len(A)
    remove_set = set(remove_order[:mid])  # mid까지의 문자들을 제거
    j = 0  # B의 인덱스

    for i in range(n):
        if i in remove_set:
            continue
        if A[i] == B[j]:
            j += 1
        if j == len(B):
            return True
    
    return False


left, right = 0, len(A)
ans = 0

while left <= right:
    mid = (left + right) // 2

    if check_substring(mid):
        left = mid + 1
        ans = left
    else:
        right = mid - 1

print(ans)
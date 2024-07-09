n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def is_subsequence():
    i = 0

    for j in range(m):
        while i < n and A[i] != B[j]:
            i += 1
        
        if i == n:
            return False
        
        else:
            i += 1
    
    return True

if is_subsequence():
    print("Yes")
else:
    print("No")
n, m = map(int, input().split())
arr = list(map(int, input().split()))

def calc(A, m):
    res = A[m - 1]

    while m > 1:
        if m % 2 == 1:
            m -= 1
        else:
            m //= 2
        res += A[m - 1]
    
    return res

print(calc(arr, m))
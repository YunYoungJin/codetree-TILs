n = int(input())

def rev_seq(n):  
    if n == 0:      
        return

    print(n, end=' ')
    rev_seq(n - 1)
    print(n, end=' ')

rev_seq(n)
N = int(input())

def sequence(n):    
    if n == 0:      
        return 

    sequence(n - 1)
    print(n, end=' ')

def reverse(n):
    if n == 0:      
        return 

    print(n, end=' ')
    reverse(n - 1)

sequence(N)
print()
reverse(N)
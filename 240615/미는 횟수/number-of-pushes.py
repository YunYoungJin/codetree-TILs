A = input()
B = input()
n = 0
leng = len(A)

while A != B:
    n += 1
    A = A[-1] + A[0:-1]
    if n == leng:
        break;

if n == leng:
    print(-1)
else:
    print(n)
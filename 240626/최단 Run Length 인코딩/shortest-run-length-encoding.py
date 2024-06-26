from collections import deque

A = deque(input())

def get_RLE_size(string):
    n = len(string)
    if n == 1:
        return 2
    
    rle = ''

    count = 1
    for i in range(n - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            rle += string[i + 1] + str(count)
            count = 1

        if i + 1 == n - 1:
            rle += string[i] + str(count)

    return len(rle)

ans = 21

for _ in range(len(A)):
    A.rotate(1)
    ans = min(ans, get_RLE_size(A))

print(ans)
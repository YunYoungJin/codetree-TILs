n, m = map(int, input().split())

global array
array = list(map(int, input().split()))

def sol(a1, a2):
    array_sum = 0
    for i in range(a1-1, a2):
        array_sum += array[i]
    return array_sum

for _ in range(m):
    a1, a2 = map(int, input().split())
    print(sol(a1, a2))
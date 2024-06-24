n = int(input())
arr = list(map(int, input().split()))

def make_abs(array):
    for i in range(len(array)):
        array[i] = abs(array[i])

make_abs(arr)
print(*arr)
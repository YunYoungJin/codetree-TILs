n = int(input())
arr = list(map(int, input().split()))

def func(array):
    for i in range(len(array)):
        if array[i] % 2 == 0:
            array[i] //= 2

func(arr)
print(*arr)
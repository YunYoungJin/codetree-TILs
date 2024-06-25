n = int(input())
arr = list(map(int, input().split()))

def find_max(arr, idx):
    if idx == 0:
        return arr[0]
    else:
        return max(find_max(arr, idx - 1), arr[idx]) 
    

print(find_max(arr, n - 1))
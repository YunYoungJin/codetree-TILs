n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def is_cs(arr1, arr2):
    if len(arr1) < len(arr2):
        return False

    elif len(arr1) == len(arr2):
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True
            
    for i in range(len(arr1)):
        exist = True
        for j in range(len(arr2)):
            if arr1[i + j] != arr2[j]:
                exist = False
                break
        if exist:
            return True
    
    return False

if is_cs(A, B):
    print("Yes")
else:
    print("No")
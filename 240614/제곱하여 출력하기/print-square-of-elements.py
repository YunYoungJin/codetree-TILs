n = int(input())
arr = list(map(int, input().split()))
new_arr = [x * x for x in arr]
print(*new_arr)
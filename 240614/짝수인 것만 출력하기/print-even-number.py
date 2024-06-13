n = int(input())
arr = list(map(int, input().split()))
new_arr = []

for num in arr:
    if num % 2 == 0:
        new_arr.append(num)
print(*new_arr)
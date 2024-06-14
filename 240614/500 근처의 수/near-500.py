arr = list(map(int, input().split()))
pivot = 500
under = 0
over = 1001

for num in arr:
    if num < pivot and under < num:
        under = num
    elif num > pivot and over > num:
        over = num
print(under, over)
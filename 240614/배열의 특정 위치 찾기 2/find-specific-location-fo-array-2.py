arr = list(map(int, input().split()))

odd_sum = 0
even_sum = 0

for i in range(10):
    if i % 2 == 0:
        even_sum += arr[i]
    else:
        odd_sum += arr[i]
print(abs(even_sum-odd_sum))
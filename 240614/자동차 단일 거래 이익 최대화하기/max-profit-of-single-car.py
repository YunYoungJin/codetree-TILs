n = int(input())
arr = list(map(int, input().split()))

max_profit = -1

for i in range(n):
    for j in range(i + 1, n):
        profit = arr[j] - arr[i]
        if profit > max_profit:
            max_profit = profit

if max_profit <= 0:
    print(0)
else:
    print(max_profit)
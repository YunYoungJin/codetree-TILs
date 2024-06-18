n = int(input())
arr = [int(input()) for _ in range(n)]

max_sum = -1
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            pos = 1
            carry = 0 
            while pos <= 10000:
                if (arr[i] // pos) % 10 + (arr[j] // pos) % 10 + (arr[k] // pos) % 10 >= 10:
                    carry = 1
                    break
                pos *= 10
            if not carry:
                max_sum = max(max_sum, arr[i] + arr[j] + arr[k])
print(max_sum)
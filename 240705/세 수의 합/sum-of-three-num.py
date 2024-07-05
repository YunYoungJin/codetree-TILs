import pprint

n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

count = dict()
ans = 0

for i in range(n):
    for j in range(i + 1, n):
        tmp = arr[i] + arr[j]
        diff = k - tmp

        if diff in count:
            ans += count[diff]

    if arr[i] in count:
        count[arr[i]] += 1
    else:
        count[arr[i]] = 1


print(ans)
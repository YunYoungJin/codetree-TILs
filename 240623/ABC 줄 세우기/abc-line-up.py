n = int(input())
arr = [
    ord(person) - ord('A')
    for person in input().split()
]

cnt = 0

if n != 1:
    for i in range(n):
        if i == arr[i]:
            continue
        else:
            idx = arr.index(i)
            while i != arr[i]:
                arr[idx], arr[idx - 1] = arr[idx - 1], arr[idx]
                cnt += 1
                idx -= 1

print(cnt)
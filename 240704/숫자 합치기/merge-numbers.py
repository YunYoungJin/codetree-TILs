n = int(input())
arr = list(map(int, input().split()))

ans = 0

while len(arr) > 1:
    arr.sort(reverse=True)
    new_num = arr.pop() + arr.pop()
    ans += new_num
    arr.append(new_num)

print(ans)
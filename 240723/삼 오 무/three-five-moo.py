n = int(input())

left = 1
right =  10 ** 20

def check(k):
    cnt1 = k // 3
    cnt2 = k // 5
    cnt3 = k // 15

    return k - (cnt1 + cnt2 - cnt3)

num = 0

while left <= right:
    mid = (left + right) // 2

    if check(mid) > n:
        right = mid - 1
    elif check(mid) < n:
        left = mid + 1
    else:
        num = mid
        break

for i in range(num, 0, -1):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
        break
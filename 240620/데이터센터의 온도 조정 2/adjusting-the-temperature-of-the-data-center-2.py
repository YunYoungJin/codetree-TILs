n, c, g, h = map(int, input().split())

work = [0] * 1001

# 장비 별 선호 온도
temp_list = [
   tuple(map(int, input().split()))
   for _ in range(n)
]

# 해당 온도일 떄 작업량
for i in range(1001):
    for temp in temp_list:
        ta, tb = temp
        if i < ta:
            work[i] += c
        elif ta <= i and i <= tb:
            work[i] += g
        else:
            work[i] += h

print(max(work))
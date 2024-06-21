n = int(input())
s = input()

length = 101

for i in range(1, n // 2 + 2):
    once = True
    for j in range(n):
        if j + i < n:
            if s.count(s[j:j + i]) >= 2:
                once = False
                break
    if once:
        length = min(length, i)

print(length)
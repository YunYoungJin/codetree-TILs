s = list(input())
n = len(s)
ans = 0
j = 0

check = set()

for i in range(n):
    while j < n and  s[j] not in check:
        check.add(s[j])
        j += 1

    ans = max(ans, len(check))

    check.remove(s[i])

print(ans)
n = int(input())
s = input()
target = input()

ans = 0
new_group = True

for i in range(n):
    if s[i] != target[i]:
        if new_group:
            ans += 1
            new_group = False
    else:
        new_group = True

print(ans)
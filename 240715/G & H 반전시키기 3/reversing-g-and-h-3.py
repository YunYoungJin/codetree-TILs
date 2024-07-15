n = int(input())
s = input()
target = input()

ans = 0
mismatched = False
group_size = 0

for i in range(n):
    if s[i] != target[i]:
        if not mismatched:
            mismatched = True
            ans += 1
            group_size += 1
        else:
            group_size += 1

            if group_size == 4:
                mismatched = False
                group_size = 0
    else:
        mismatched = False

print(ans)
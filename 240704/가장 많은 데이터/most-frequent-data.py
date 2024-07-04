n = int(input())
freq = dict()

for _ in range(n):
    s = input()
    if s not in freq:
        freq[s] = 1
    else:
        freq[s] += 1

ans = 0
for v in freq.values():
    ans = max(ans, v)
print(ans)
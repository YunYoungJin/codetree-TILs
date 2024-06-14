n = int(input())
s = [input() for _ in range(n)]
c = input()
cnt = 0
len_sum = 0

for word in s:
    if word[0] == c:
        cnt += 1
        len_sum += len(word)

print(cnt, f"{len_sum/cnt:.2f}")
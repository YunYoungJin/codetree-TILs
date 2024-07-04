n = int(input())
group = dict()

ans = 0
for _ in range(n):
    word = list(input())
    word.sort()

    sorted_word = ''.join(word)
    if sorted_word not in group:
        group[sorted_word] = 1
    else:
        group[sorted_word] += 1

    ans = max(ans, group[sorted_word])

print(ans)
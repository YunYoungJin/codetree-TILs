n, k = map(int, input().split())

line = [''] * 10001

for _ in range(n):
    s = input().split()
    line[int(s[0])] = s[1]

max_score = 0

for i in range(1, 10001 - k):
    score = 0
    for j in range(i, i + k + 1):
        if line[j] == 'G':
            score += 1
        elif line[j] == 'H':
            score += 2

    max_score = max(max_score, score)

print(max_score)
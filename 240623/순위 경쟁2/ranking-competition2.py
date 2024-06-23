n = int(input())

first_rank = 'both'

cnt = 0
score_a = 0
score_b = 0

for _ in range(n):
    c, s = input().split() 
    s = int(s)

    if c == 'A':
        score_a += s
    else:
        score_b += s

    if score_a > score_b and first_rank != 'A':
        cnt += 1
        first_rank = 'A'
    elif score_a < score_b and first_rank != 'B':
        cnt += 1
        first_rank = 'B'
    elif score_a == score_b and first_rank != 'both':
        cnt += 1
        first_rank = 'both'

print(cnt)
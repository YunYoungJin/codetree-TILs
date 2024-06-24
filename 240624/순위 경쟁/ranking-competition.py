n = int(input())

first_rank = 'all'

cnt = 0
score_a = 0
score_b = 0
score_c = 0

for _ in range(n):
    c, s = input().split() 
    s = int(s)

    if c == 'A':
        score_a += s
    elif c == 'B':
        score_b += s
    else:
        score_c += s

    if score_a > score_b and score_a > score_c and first_rank != 'A':
        cnt += 1
        first_rank = 'A'
    elif score_b > score_a and score_b > score_c and first_rank != 'B':
        cnt += 1
        first_rank = 'B'
    elif score_c > score_a and score_c > score_b and first_rank != 'C':
        cnt += 1
        first_rank = 'C'
    elif score_a == score_b and score_a > score_c and first_rank != 'A B':
        cnt += 1
        first_rank = 'A B'
    elif score_a == score_c and score_a > score_b and first_rank != 'A C':
        cnt += 1
        first_rank = 'A C'
    elif score_b == score_c and score_b > score_a and first_rank != 'B C':
        cnt += 1
        first_rank = 'B C'
    elif score_a == score_b and score_b == score_c and first_rank != 'all':
        cnt += 1
        first_rank = 'all'

print(cnt)
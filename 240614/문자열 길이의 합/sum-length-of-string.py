n = int(input())

a_cnt = 0
len_sum = 0
for _ in range(n):
    s = input()
    if s[0] == 'a':
        a_cnt += 1
    len_sum += len(s)
print(len_sum, a_cnt)
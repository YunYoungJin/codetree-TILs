s = input()
order = input()
L_cnt = order.count('L')
R_cnt = order.count('R')

if L_cnt - R_cnt > 0:
    for _ in range(L_cnt - R_cnt):
        s = s[1:] + s[0]
elif L_cnt - R_cnt < 0:
    for _ in range(R_cnt - L_cnt):
        s = s[-1] + s[0:-1]
print(s)
import sys
INT_MIN = -sys.maxsize

s = list(input())
alpha = s[0::2]
opers = s[1::2]

alpha_set = list(set(alpha))
alpha_match = [0] * 6
d = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5}

ans = INT_MIN

def calc():
    global ans
    res = alpha_match[d[alpha[0]]]
    for i in range(1, len(alpha)):
        if opers[i - 1] == '+':
            res += alpha_match[d[alpha[i]]]
        elif opers[i - 1] == '-':
            res -= alpha_match[d[alpha[i]]]
        elif opers[i - 1] == '*':
            res *= alpha_match[d[alpha[i]]]
        else:
            res /= alpha_match[d[alpha[i]]]
    
    ans = max(ans, res)

def choose(cnt):
    if cnt == len(alpha_set):
        calc()
        return
    
    for i in range(1, 5):
        alpha_match[d[alpha_set[cnt]]] = i
        choose(cnt + 1)
        alpha_match[d[alpha_set[cnt]]] = 0

choose(0)
print(ans)
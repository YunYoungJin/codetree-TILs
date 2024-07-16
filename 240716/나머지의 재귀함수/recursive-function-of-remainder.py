n = int(input())
memo = [-1] * (n + 1)

memo[1] = 2
memo[2] = 4

def find_num(n):
    if memo[n] != -1:
        return memo[n]

    memo[n] = (find_num(n - 1) * find_num(n - 2)) % 100
    return memo[n]

find_num(n)
print(memo[n])
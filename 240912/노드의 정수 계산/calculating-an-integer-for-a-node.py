import sys
from collections import defaultdict
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
tree = defaultdict(list)
dp = [0] * (n + 1)

for i in range(2, n + 1):
    t, a, p = map(int, input().split())
    
    if t == 1:
        dp[i] = a
    else:
        dp[i] = -a

    tree[p].append(i)

def dfs(node):
    for child in tree[node]:
        dfs(child)

        if dp[child] > 0:
            dp[node] += dp[child]

dfs(1)
print(dp[1])
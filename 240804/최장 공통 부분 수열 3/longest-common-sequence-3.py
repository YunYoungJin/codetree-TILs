import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

MAX = max(n, m) + 1
dp = [[-1 for _ in range(MAX)] for _ in range(MAX)]
lcslen = 0
found = False

def compute_lcs(a, b, i, j):
    """Compute the length of LCS for a[i:] and b[j:]"""
    if i == n or j == m:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if a[i] == b[j]:
        dp[i][j] = 1 + compute_lcs(a, b, i + 1, j + 1)
    else:
        dp[i][j] = max(compute_lcs(a, b, i + 1, j),
                      compute_lcs(a, b, i, j + 1))
    return dp[i][j]

def find_smallest_lcs(a, b, idx1, idx2, curr_lcs, data):
    """Find the smallest lexicographical LCS"""
    global found

    if curr_lcs == lcslen:
        print(" ".join(map(str, data[:curr_lcs])))
        found = True
        return

    if idx1 == n or idx2 == m:
        return

    for num in sorted(set(a[idx1:])):
        if found:
            return

        done = False
        for i in range(idx1, n):
            if num == a[i]:
                for j in range(idx2, m):
                    if num == b[j] and dp[i][j] == lcslen - curr_lcs:
                        data[curr_lcs] = num
                        find_smallest_lcs(a, b, i + 1, j + 1, curr_lcs + 1, data)
                        done = True
                        break
                if done:
                    break

def find_smallest_lcs_sorted(a, b):
    """Find and print the smallest lexicographical LCS of a and b"""
    global lcslen, found
    lcslen = compute_lcs(a, b, 0, 0)
    data = [0 for _ in range(MAX)]
    found = False
    find_smallest_lcs(a, b, 0, 0, 0, data)


find_smallest_lcs_sorted(a, b)
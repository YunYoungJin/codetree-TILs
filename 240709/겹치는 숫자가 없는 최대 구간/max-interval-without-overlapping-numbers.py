n = int(input())
arr = [0] + list(map(int, input().split()))

ans = 0
visited = [False] * 100001
j = 0

for i in range(1, n + 1):
    while j + 1 <= n and not visited[arr[j + 1]]:
        visited[arr[j + 1]] = True
        j += 1
    
    ans = max(ans, j - i + 1)

    visited[arr[i]] = False

print(ans)
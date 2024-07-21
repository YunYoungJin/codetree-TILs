n, m = map(int, input().split())
fires = list(map(int, input().split()))
stations = list(map(int, input().split()))
fires.sort()
stations.sort()

ans = 0
j = 0

for i in range(n):
    while j < m - 1 and abs(stations[j + 1] - fires[i]) <= abs(stations[j] - fires[i]):
        j += 1
    
    ans = max(ans, abs(stations[j] - fires[i]))

print(ans)
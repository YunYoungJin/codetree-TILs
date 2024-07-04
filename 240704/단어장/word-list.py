from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()

for _ in range(n):
    s = input()
    if s not in sd:
        sd[s] = 1
    else:
        sd[s] += 1
        
for key, value in sd.items():
    print(key, value)
from sortedcontainers import SortedDict

n = int(input())
arr = list(map(int, input().split()))
sd = SortedDict()

for idx, num in enumerate(arr):
    if num not in sd:
        sd[num] = idx + 1

for key, value in sd.items():
    print(key, value)
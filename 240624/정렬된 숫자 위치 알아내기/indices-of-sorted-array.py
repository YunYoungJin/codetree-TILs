n = int(input())

nums = list(map(int, input().split()))
pos_infos = []

for idx, num in enumerate(nums, start = 1):
    pos_infos.append([num, idx, -1])

pos_infos.sort(key = lambda x : x[0])

for i in range(n):
    pos_infos[i][2] = i + 1

pos_infos.sort(key = lambda x : x[1])

for info in pos_infos:
    print(info[2], end=' ')
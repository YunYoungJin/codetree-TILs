n = int(input())
arr = list(map(int, input().split()))
res = [0] * 1001
satisfied = False

for num in arr:
    res[num] += 1

for i in range(1000, 0, -1):
    if res[i] == 1:
        print(i)
        satisfied = True
        break
if not satisfied:
    print(-1)
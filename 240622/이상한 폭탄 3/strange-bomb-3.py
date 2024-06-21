n, k = map(int, input().split())

bomb_list = [
    int(input())
    for _ in range(n)
]

exploded = [0] * 1000001
check = [False for _ in range(n)]
bomb_num_list = list(set(bomb_list))

for bomb_num in bomb_num_list:
    for i in range(n):
        if bomb_list[i] != bomb_num:
            continue

        for j in range(i + 1, n):
            if bomb_list[j] != bomb_num:
                continue
            
            if j - i <= k:
                if not check[i] and not check[j]:
                    check[i] = True
                    check[j] = True
                    exploded[bomb_num] += 2
                elif check[i] and not check[j]:
                    check[j] = True
                    exploded[bomb_num] += 1

largest = max(exploded)

if largest == 0:
    print(0)
else:
    exploded.reverse()
    print(1000000 - exploded.index(largest))
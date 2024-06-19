n = int(input())
nums = [
    list(map(int, input().split()))
    for _ in range(2)
]

num_list = [i for i in range(1, n + 1)]

ans = []

for num in nums:
    a, b, c = num
    idx_a = num_list.index(a)
    idx_b = num_list.index(b)
    idx_c = num_list.index(c)

    for i in range(idx_a - 2, idx_a + 3):
        for j in range(idx_b - 2, idx_b + 3):
            for k in range(idx_c - 2, idx_c + 3):
                comb = [num_list[i], num_list[j], num_list[k]]
                if comb not in ans:
                    ans.append(comb)
print(len(ans))
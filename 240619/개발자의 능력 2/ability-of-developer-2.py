import sys
numbers = list(map(int, input().split()))

def get_diff(i, j, k, l):
    idxs = [i, j, k, l]

    group_sum = numbers[i] + numbers[j] + numbers[k] + numbers[l]
    sum3 = sum(numbers) - group_sum

    in_diff = sys.maxsize
    for p in range(4):
        for q in range(p + 1, 4):
            sum1 = numbers[p] + numbers[q]
            sum2 = group_sum - sum1
            diff = max(sum1, sum2, sum3) - min(sum1, sum2, sum3)
            in_diff = min(in_diff, diff)
    return in_diff

min_diff = sys.maxsize
for i in range(0, 6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            for l in range(k + 1, 6):
                min_diff = min(min_diff, get_diff(i, j, k, l))

print(min_diff)
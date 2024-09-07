import heapq
from sortedcontainers import SortedSet

n, m = map(int, input().split())
removals = list(map(int, input().split()))

index = SortedSet([0, n])
length_dict = {n + 1: 1}
max_length = n + 1

def update_length(length):
    global max_length
    if length in length_dict:
        length_dict[length] += 1
    else:
        length_dict[length] = 1
    if length > max_length:
        max_length = length

def remove_length(length):
    global max_length
    if length in length_dict:
        length_dict[length] -= 1
        if length_dict[length] == 0:
            del length_dict[length]
            if length == max_length:
                if length_dict:
                    max_length = max(length_dict)
                else:
                    max_length = 0

for num in removals:
    left = index.bisect_left(num) - 1
    right = index.bisect_right(num)

    left_boundary = index[left]
    right_boundary = index[right]

    if left_boundary == 0 and right_boundary == n:
        old_length = right_boundary - left_boundary + 1

    elif left_boundary == 0:
        old_length = right_boundary - left_boundary

    elif right_boundary == n:
        old_length = right_boundary - left_boundary

    else:
        old_length = right_boundary - left_boundary - 1

    remove_length(old_length)
    l1 = num - left_boundary - (0 if left_boundary == 0 else 1)
    l2 = right_boundary - num - (0 if right_boundary == n else 1)

    index.add(num)
    update_length(l1)
    update_length(l2)

    print(max_length)
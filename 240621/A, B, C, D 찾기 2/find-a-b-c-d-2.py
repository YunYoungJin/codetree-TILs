arr = list(map(int, input().split()))

def is_equal_array(arr1, arr2):
    arr1.sort()
    arr2.sort()

    if len(arr1) != len(arr2):
        return False

    for x, y in zip(arr1, arr2):
        if x != y:
            return False

    return True

for a in range(1, 11):
    for b in range(a, 14):
        for c in range(b, 20):
            for d in range(c, 37):
                comb = [
                            a, b, c, d, \
                            a + b, b + c, c + d, d + a, a + c, b + d, \
                            a + b + c, a + b + d, a + c + d, b + c + d, \
                            a + b + c + d
                        ]
                if is_equal_array(comb, arr):
                    print(a, b, c, d)
                    break
n, m, c = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
ans = 0

def get_max_value(region):
    max_value = 0

    def maximize_value(index, current_weight, current_value):
        nonlocal max_value
        if current_weight > c:
            return
        if index == len(region):
            max_value = max(max_value, current_value)
            return
        # 선택하지 않는 경우
        maximize_value(index + 1, current_weight, current_value)
        # 선택하는 경우
        maximize_value(index + 1, current_weight + region[index], current_value + region[index] ** 2)

    maximize_value(0, 0, 0)
    return max_value


def calc(first_region, second_region):
    global ans
    first_max_value = get_max_value(first_region)
    second_max_value = get_max_value(second_region)
    ans = max(ans, first_max_value + second_max_value)
    return


for row1 in range(n):
    for col1 in range(n - m + 1):
        first_region = grid[row1][col1:col1 + m]
        for row2 in range(row1, n):
            if row1 != row2:
                start_col2 = 0
            else:
                start_col2 = col1 + m

            if start_col2 + m - 1 >= n:
                continue

            for col2 in range(start_col2, n - m + 1):
                second_region = grid[row2][col2:col2 + m]
                calc(first_region, second_region)

print(ans)
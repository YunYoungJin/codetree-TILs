def slide_and_merge(row):
    filtered_row = [num for num in row if num != 0]
    
    new_row = [0] * 4
    index = 0  # 새 행에 숫자를 추가할 위치
    skip = False  # 합치기 방지 플래그

    for i in range(len(filtered_row)):
        if skip:
            skip = False
            continue
        
        if i < len(filtered_row) - 1 and filtered_row[i] == filtered_row[i + 1]:
            # 합칠 수 있는 경우
            new_row[index] = filtered_row[i] * 2
            index += 1
            skip = True  # 다음 숫자는 스킵
        else:
            new_row[index] = filtered_row[i]
            index += 1
    
    return new_row

def move_left(grid):
    return [slide_and_merge(row) for row in grid]


def move_right(grid):
    return [slide_and_merge(row[::-1])[::-1] for row in grid]


def move_up(grid):
    # 전치(transpose) 후 왼쪽으로 이동, 다시 전치
    transposed_grid = list(zip(*grid))
    moved_grid = move_left([list(row) for row in transposed_grid])
    return list(zip(*moved_grid))


def move_down(grid):
    # 전치(transpose) 후 오른쪽으로 이동, 다시 전치
    transposed_grid = list(zip(*grid))
    moved_grid = move_right([list(row) for row in transposed_grid])
    return list(zip(*moved_grid))


def print_grid(grid):
    for row in grid:
        print(*row)


grid = [
    list(map(int, input().split()))
    for _ in range(4)
]
direction = input()

# 방향에 따른 이동
if direction == 'L':
    result_grid = move_left(grid)
elif direction == 'R':
    result_grid = move_right(grid)
elif direction == 'U':
    result_grid = move_up(grid)
elif direction == 'D':
    result_grid = move_down(grid)

# 결과 출력
print_grid(result_grid)
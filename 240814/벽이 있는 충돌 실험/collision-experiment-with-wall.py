from collections import deque


def simulate(n, beads):
    direction_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    opposite_direction = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

    for _ in range(2 * n):
        cnt = len(beads)
        visited = set()
        collision_cnt = 0

        for _ in range(cnt):
            curr_x, curr_y, d = beads.popleft()

            dx, dy = direction_map[d]
            new_x, new_y = curr_x + dx, curr_y + dy

            if not (0 <= new_x < n and 0 <= new_y < n):
                # 벽에 부딪히면 방향 반전
                d = opposite_direction[d]
                new_x, new_y = curr_x, curr_y

            if (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                beads.append((new_x, new_y, d))
            else:
                collision_cnt += 1

        check = 0
        while beads and check < collision_cnt:
            x, y, d = beads.popleft()
            if (x, y) in visited:
                check += 1
            else:
                beads.append((x, y, d))

    # 남아있는 구슬의 수 계산
    remaining_beads = len(beads)
    return remaining_beads


# 입력 처리 및 시뮬레이션
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    beads = deque()
    for _ in range(m):
        x, y, d = input().split()
        x, y = int(x) - 1, int(y) - 1
        beads.append((x, y, d))

    print(simulate(n, beads))
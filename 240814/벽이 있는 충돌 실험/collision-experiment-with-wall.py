from collections import deque, defaultdict

t = int(input())

def simulate(n, beads):
    direction_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    # 이동 및 충돌 처리
    for _ in range(2 * n):
        to_remove = set()  # 충돌로 사라질 구슬의 위치를 기록
        visited = defaultdict(list)  # 구슬의 위치를 기록

        for idx in range(len(beads)):
            x, y, d = beads[idx]
            dx, dy = direction_map[d]
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < n and 0 <= new_y < n:
                if (new_x, new_y) in visited:
                    to_remove.add((new_x, new_y))
                visited[(new_x, new_y)].append((d, (x, y)))
            else:
                # 벽에 부딪혀 방향 반전
                if d == 'U': d = 'D'
                elif d == 'D': d = 'U'
                elif d == 'L': d = 'R'
                elif d == 'R': d = 'L'
                new_x, new_y = x, y  # 이동하지 않음
                if (new_x, new_y) in visited:
                    to_remove.add((new_x, new_y))
                visited[(new_x, new_y)].append((d, (x, y)))

        beads.clear()

        # 충돌 처리 후 남은 구슬을  업데이트
        for pos, items in visited.items():
            if pos not in to_remove:
                for d, original_pos in items:
                    beads.append((pos[0], pos[1], d))


    # 남아있는 구슬의 수 계산
    remaining_beads = len(beads)
    return remaining_beads

for _ in range(t):
    n, m = map(int, input().split())
    beads = []
    for _ in range(m):
        x, y, d = input().split()
        x, y = int(x) - 1, int(y) - 1
        beads.append((x, y, d))

    print(simulate(n, beads))
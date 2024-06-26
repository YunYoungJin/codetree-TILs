n, m = map(int, input().split())

origin = [int(input()) for _ in range(n)]


def check_explosion(bombs):
    after_exp = []
    if len(bombs) == 0:
        return after_exp

    curr_bomb = bombs[0]
    bomb_cnt = 1

    for target_bomb in bombs[1:]:
        if target_bomb == curr_bomb:
            bomb_cnt += 1
        else:
            if bomb_cnt < m:
                for _ in range(bomb_cnt):
                    after_exp.append(curr_bomb)

            curr_bomb = target_bomb
            bomb_cnt = 1

    if bomb_cnt < m:
        for _ in range(bomb_cnt):
            after_exp.append(curr_bomb)

    return after_exp


while True:
    temp = check_explosion(origin)

    if origin == temp:
        break
    else:
        origin = temp

cnt = len(origin)
print(cnt)
if cnt != 0:
    for bomb in origin:
        print(bomb)
n, m, k = map(int, input().split())
turns = list(map(int, input().split()))

combi = []
score = 0

def check_points():
    result = [1] * (k + 1)

    for turn, piece in zip(turns, combi):
        result[piece] += turn
    
    tmp = 0
    for i in range(1, k + 1):
        if result[i] >= m:
            tmp += 1

    global score
    score = max(score, tmp)

def select_piece(curr_pos):
    if curr_pos == n + 1:
        check_points()
        return

    for i in range(1, k + 1):
        combi.append(i)
        select_piece(curr_pos + 1)
        combi.pop()

select_piece(1)
print(score)
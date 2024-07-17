import heapq

n = int(input())
infos = []

for i in range(n):
    a, t = map(int, input().split())
    infos.append((a, t, i))

infos.sort(key=lambda x: (x[0], x[2]))

waiting_time = [0] * n
waiting_list = []

last_exit_time = 0
ans = 0

for a, t, i in infos:
    # 이전 사람의 퇴장 시간보다 일찍 도착했다면 대기열에 추가
    if a < last_exit_time:
        heapq.heappush(waiting_list, (i, a, t))

    else:
        # 나중에 도착했고 대기열에 사람이 없다면
        if not waiting_list:
            last_exit_time = a + t

        # 나중에 도착했지만 대기열에 사람이 있다면
        else:
            while waiting_list:
                next_i, next_a, next_t = waiting_list[0]
                if last_exit_time + next_t <= a:
                    heapq.heappop(waiting_list)
                    waiting_time[next_i] = last_exit_time - next_a
                    last_exit_time += next_t
                    if not waiting_list:
                        last_exit_time = a + t
                else:
                    heapq.heappush(waiting_list, (i, a, t))
                    break

while waiting_list:
    next_i, next_a, next_t = heapq.heappop(waiting_list)
    waiting_time[next_i] = last_exit_time - next_a
    last_exit_time += next_t

print(max(waiting_time))
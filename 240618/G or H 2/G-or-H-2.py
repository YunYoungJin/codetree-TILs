n = int(input())

line = [''] * 101

for _ in range(n):
    s = input().split()
    line[int(s[0])] = s[1]

if n == 1:
    print(0)
else:
    max_size = 0

    for i in range(len(line)):
        # 왼쪽에 알파벳을 들고 있는 사람이 없으면 skip
        if line[i] == '':
            continue

        # 가장 왼쪽 사람의 알파벳 카운트
        g_cnt, h_cnt = 0, 0
        if line[i] == 'G':
            g_cnt += 1
        else:
            h_cnt += 1

        for j in range(i + 1, len(line)):
            if line[j] == 'G':
                g_cnt += 1
            elif line[j] == 'H':
                h_cnt += 1
            else:
                continue

            if (g_cnt == 0 and h_cnt != 0) or (g_cnt != 0 and h_cnt == 0) or (g_cnt == h_cnt):
                size = j - i 
                max_size = max(max_size, size)

    print(max_size)
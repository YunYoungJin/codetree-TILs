n = int(input())
s = input()

length = 101

# 부분 문자열 길이가 i일 때
for i in range(1, n + 1):
    once = True
    # 부분 문자열의 시작 index가 j
    for j in range(n):
        # 부분 문자열이 생성 가능하면
        if j + i <= n:
            cnt = 0
            sub = s[j:j + i]
            for k in range(len(s) - i + 1):
                if s[k:k + i] == sub:
                    cnt += 1
            if cnt != 1:
                once = False
                break
    if once:
        length = min(length, i)

print(length)
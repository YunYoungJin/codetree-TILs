s = input()
rle = ''
c = s[0]
cnt = 0

for i in range(len(s)):
    if s[i] == c:
        cnt += 1
    else:
        rle = rle + c + str(cnt)
        c = s[i]
        cnt = 1
    if i == len(s) - 1:
        rle = rle + c + str(cnt)
print(len(rle))
print(rle)
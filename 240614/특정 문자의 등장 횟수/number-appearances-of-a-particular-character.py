s = input()
cnt1 = 0
cnt2 = 0

for i in range(len(s)-1):
    if s[i:i+2] == 'ee':
        cnt1 += 1
    if s[i:i+2] == 'eb':
        cnt2 += 1
print(cnt1, cnt2)
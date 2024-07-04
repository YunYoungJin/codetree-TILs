s = input()
freq = dict()

for c in s:
    if c not in freq:
        freq[c] = 1
    else:
        freq[c] += 1

for i in range(len(s)):
    if freq[s[i]] == 1:
        print(s[i])
        break
    
    if i == len(s) - 1:
        print("None")
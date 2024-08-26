from collections import defaultdict

s, k = input().split()
s = list(s)
n = len(s)
k = int(k)

char_count = defaultdict(int)
left = 0
max_length = 0

for right in range(n):
    char_count[s[right]] += 1
    
    # 서로 다른 문자의 개수가 k를 넘으면 왼쪽 포인터 이동
    while len(char_count) > k:
        char_count[s[left]] -= 1
        if char_count[s[left]] == 0:
            del char_count[s[left]]
        left += 1
    
    max_length = max(max_length, right - left + 1)

print(max_length)
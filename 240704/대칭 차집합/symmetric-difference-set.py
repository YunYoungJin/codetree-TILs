n, m = map(int, input().split())
s1 = set(list(map(int, input().split())))
s2 = set(list(map(int, input().split())))

print(len((s1 - s2) | (s2 - s1)))
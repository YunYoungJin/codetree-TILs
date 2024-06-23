a, b, x, y = map(int, input().split())

# 순간 이동 안하는 경우
s = abs(b - a)

# 순간 이동 x -> y로 하는 경우
s = min(s, abs(a - x) + abs(b - y))

# 순간 이동 y -> x로 하는 경우
s = min(s, abs(a - y) + abs(b - x))

print(s)
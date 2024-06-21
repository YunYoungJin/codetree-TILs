import sys

n = int(input())

points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

is_possible = False

# 가로, 세로 0, 3
for i in range(11):
    for j in range(11):
        for k in range(11):
            # 각 직선 조합마다 가능성 체크
            passed = False
            # 모든 점에 대해서
            for x, y in points:
                if x == i or x == j or x == k:
                    passed = True
                # 한 점이라도 불가능하면 다음 조합
                if not passed:
                    break
            # 가능하면
            if passed:
                print(1)
                sys.exit(0)

# 가로, 세로 1, 2
for i in range(11):
    for j in range(11):
        for k in range(11):
            # 각 직선 조합마다 가능성 체크
            passed = False
            # 모든 점에 대해서
            for x, y in points:
                if x == i or x == j or y == k:
                    passed = True
                # 한 점이라도 불가능하면 다음 조합
                if not passed:
                    break
            # 가능하면
            if passed:
                print(1)
                sys.exit(0)


# 가로, 세로 2, 1
for i in range(11):
    for j in range(11):
        for k in range(11):
            passed = False
            for x, y in points:
                if x == i or y == j or y == k:
                    passed = True
                if not passed:
                    break
            if passed:
                print(1)
                sys.exit(0)

# 가로, 세로 3, 0
for i in range(11):
    for j in range(11):
        for k in range(11):
            # 각 직선 조합마다 가능성 체크
            passed = False
            # 모든 점에 대해서
            for x, y in points:
                if y == i or y == j or y == k:
                    passed = True
                # 한 점이라도 불가능하면 다음 조합
                if not passed:
                    break
            # 가능하면
            if passed:
                print(1)
                sys.exit(0)


# 모든 경우에 pass하지 않았다면
print(0)
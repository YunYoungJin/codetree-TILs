from sortedcontainers import SortedSet
import sys
input = sys.stdin.readline

problems = SortedSet()
n = int(input())
for _ in range(n):
    P, L = map(int, input().split())
    problems.add((L, P))

m = int(input())
for _ in range(m):
    command = input().split()
    if command[0] == "ad":
        # 문제 추가: ad P L
        P = int(command[1])
        L = int(command[2])
        problems.add((L, P))
    elif command[0] == "sv":
        # 문제 제거: sv P L
        P = int(command[1])
        L = int(command[2])
        problems.discard((L, P))
    elif command[0] == "rc":
        # 최고/최저 난이도 문제 출력: rc x
        x = int(command[1])
        if x == 1:
            # 가장 높은 난이도의 문제 번호 출력
            print(problems[-1][1])  # 난이도가 가장 높은 문제의 번호
        else:
            # 가장 낮은 난이도의 문제 번호 출력
            print(problems[0][1])  # 난이도가 가장 낮은 문제의 번호
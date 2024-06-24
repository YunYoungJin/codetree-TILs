n = int(input())

infos = [
    tuple(input().split())
    for _ in range(n)
]

infos.sort(key = lambda x : int(x[1]) + int(x[2]) + int(x[3]))

for name, kor, eng, math in infos:
    print(f"{name} {kor} {eng} {math}")
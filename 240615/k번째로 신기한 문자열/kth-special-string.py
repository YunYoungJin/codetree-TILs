n, k, T = input().split()
arr = []

for _ in range(int(n)):
    s = input()
    if s[:len(T)] == T:
        arr.append(s)
arr.sort()
print(arr[int(k) - 1])
s = [input() for _ in range(10)]
c = input()
exists = False

for word in s:
    if word[-1] == c:
        print(word)
        exists = True

if not exists:
    print("None")
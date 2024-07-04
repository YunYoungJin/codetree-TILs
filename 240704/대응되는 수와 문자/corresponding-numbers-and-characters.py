n, m = map(int, input().split())
str_dict = dict()
index_dict = dict()

for i in range(n):
    s = input()
    str_dict[s] = i + 1
    index_dict[i + 1] = s

for _ in range(m):
    query = input()
    if query in str_dict: 
        print(str_dict[query])
    else:
        print(index_dict[int(query)])
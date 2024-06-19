n = int(input())

B = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 유추 가능한 숫자 초기화
nums = []
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and k != i:
                nums.append(str(i) + str(j) + str(k))

for ask in B:
    guess, s, b = ask
    guess = str(guess)
    
    for num in nums.copy():
        sn, bn = 0, 0
        for i in range(0, 3):
            for j in range(0, 3):
                if (num[i] == guess[j]) and i == j:
                    sn += 1
                elif (num[i] == guess[j]) and i != j:
                    bn += 1
        if s != sn or b != bn:
            nums.remove(num)

print(len(nums))
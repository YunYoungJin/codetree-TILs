score = list(map(float, input().split()))

avg = sum(score)/len(score)
print(f"{avg:.1f}")
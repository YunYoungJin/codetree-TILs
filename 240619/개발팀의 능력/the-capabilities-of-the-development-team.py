import sys
nums = list(map(int, input().split()))

def get_diff(t1, t2, t3):
	# 최대 능력의 팀과 최소 능력의 팀간의 능력 차이를 리턴
    max_team = max(t1, t2, t3)
    min_team = min(t1, t2, t3)

    return max_team - min_team

min_diff = sys.maxsize
possible = False

# 1번 팀 2명 구성
for i in range(0, 5):
    for j in range(i + 1, 5):
        # 2번 팀 1명 구성
        for k in range(0, 5):
            # 1번 팀 팀원과 겹치지 않게
            if k == i or k == j:
                continue

            sum1 = nums[i] + nums[j]
            sum2 = nums[k]
            
            # 팀간 능력치가 같지않도록 확인
            if sum1 == sum2:
                continue
            
            sum3 = sum(nums) - sum1 - sum2
            
            if sum3 == sum1 or sum3 == sum2:
                continue
            
            possible = True
            min_diff = min(min_diff, get_diff(sum1, sum2, sum3))

print(min_diff if possible else -1)
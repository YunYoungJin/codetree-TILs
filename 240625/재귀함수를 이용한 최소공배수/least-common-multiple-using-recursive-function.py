n = int(input())
arr = list(map(int, input().split()))

def lcm(a, b):
  t = a % b
  if t == 0:
    return a
  return a * lcm(b, t) // t

def find_lcm_of_arr(idx):
    if idx == 0:
        return arr[0]

    return lcm(find_lcm_of_arr(idx - 1), arr[idx])


print(find_lcm_of_arr(n - 1))
def bubble_sort(a):
  sorted_flag = False
  
  while sorted_flag == False:
    sorted_flag = True
    for i in range(len(a) - 1):
      if a[i] > a[i + 1]:
        tmp = a[i]
        a[i] = a[i + 1]
        a[i + 1] = tmp
        sorted_flag = False

  return a

n = int(input())
arr = list(map(int, input().split()))
arr = bubble_sort(arr)
print(*arr)
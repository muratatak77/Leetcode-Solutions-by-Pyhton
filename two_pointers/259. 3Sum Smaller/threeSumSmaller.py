def triplet_with_smaller_sum(arr, target):
  arr.sort()
  count = 0
  #we can take len(arr) - 2 , because we have 2 pointer left and right. 
  for i in range(len(arr)-2):
    count += search_pair(arr, target, i)
  return count


def search_pair(arr, target, i):
  count = 0
  left, right = i + 1, len(arr) - 1
  while (left < right):
    if  arr[i] + arr[left] + arr[right] < target:  # found the triplet
      count += right - left
      left += 1
    else:
      right -= 1  # we need a pair with a smaller sum
  return count


def main():
  # print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  # print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))
  print(triplet_with_smaller_sum([-2,0,1,3], 2))

main()


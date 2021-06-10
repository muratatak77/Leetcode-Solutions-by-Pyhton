from collections import deque


def find_subarrays(arr, target):
  result = []
  product = 1
  left = 0
  for right in range(len(arr)):
    print("right : ", right, " / left : ", left)
    product *= arr[right]
    print("product : ", product)

    while (product >= target and left < len(arr)):
      product /= arr[left]
      print("         product /:", product)
      left += 1
      print("         left :", left)

    # since the product of all numbers from left to right is less than the target therefore,
    # all subarrays from left to right will have a product less than the target too; to avoid
    # duplicates, we will start with a subarray containing only arr[right] and then extend it
    temp_list = deque()
    for i in range(right, left-1, -1):
      temp_list.appendleft(arr[i])
      print("-------")
      print("           temp_list " , temp_list)
      result.append(list(temp_list))
      print("           result : ", result)
    print("----------------------------------")
  return result


def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  # print(find_subarrays([8, 2, 6, 5], 50))


main()
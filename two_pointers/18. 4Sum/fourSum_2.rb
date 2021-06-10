
def four_sum(nums, target)


  def start_process(nums, target)
    result = []
    for i in (0..nums.length-3)
      if i > 0 and nums[i] == nums[i-1]
        next
      end
      for j in (i+1..nums.length-2)
        if j > i+1 and nums[j] == nums[j-1]
          next
        end
        search_pairs(nums, target, i,j, result)
      end
    end
    return result
  end


  def search_pairs(nums, target, first,second, result)
    left = second+1
    right = nums.length-1

    while left < right
      _sum = nums[first] + nums[second] + nums[left] + nums[right]
      if _sum == target
        result.append([nums[first], nums[second], nums[left], nums[right] ])
        left += 1
        right -= 1
        while left < right and nums[left] == nums[left-1]
          left += 1
        end
        while left < right and nums[right] == nums[right+1]
          right -= 1
        end
      elsif _sum < target
        left += 1
      else
        right -=1
      end
    end
  end

  nums = nums.sort()
  return start_process(nums, target)
end


# def main():
#   print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
#   # print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))

# main()
nums = [1,0,-1,0,-2,2]
target = 0


nums = [-1,0,-5,-2,-2,-4,0,1,-2]
target  = -9


res = four_sum(nums, target)
print("res : ", res)
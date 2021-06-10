def longest_ones(nums, k)

  # we need to keep ones count
  # for sliding window we need to keep window_start
  ones_count = 0
  window_start = 0
  max_length = 0

  for window_end in (0..nums.length-1)
    #save ones_count.
    ones_count += 1 if nums[window_end] == 1

    #check whether need shrink the window or not
    #if we have 0's grater than 'k', we need to shrink.
    #our equation for sliding window : (window_end - window_start + 1)
    #but we need substruction 1's count to find 0's count
    if (window_end - window_start + 1 - ones_count) > k
      ones_count -= 1 if nums[window_start] == 1
      window_start += 1
    end

    max_length = [max_length, window_end - window_start + 1].max
  end

  return max_length

end

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2


# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3
res = longest_ones(nums, k)
print("res : ", res)

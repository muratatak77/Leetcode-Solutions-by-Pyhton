def min_sub_array_len(arr, s)
  
  window_sum = 0
  min_lenght = 1 << 64
  window_start = 0
  n = arr.length

  for window_end in 0..n-1
    window_sum += arr[window_end]
    while window_sum >= s do
      min_lenght = [min_lenght, window_end-window_start+1].min
      window_sum -= arr[window_start]
      window_start += 1
    end
  end

  return 0 if min_lenght == 1 << 64
  return min_lenght

end

arr = [2, 1, 5, 2, 3, 2]
arr = [2, 1, 5, 2, 8]
s=7 
res = min_sub_array_len(arr, s)
puts "res : #{res}"
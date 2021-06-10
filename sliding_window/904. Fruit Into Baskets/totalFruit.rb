def total_fruit(tree)

	window_start = 0
	freq_map = {}
	max_lenght = 0

	for window_end in (0..tree.length)
		
		right_fruit = tree[window_end]
		unless freq_map.include? right_fruit
			freq_map[right_fruit] = 0
		end
		freq_map[right_fruit] += 1
		puts("freq_map : #{freq_map}")

		#shrink the sliding window, until we are left with 2 fruits in the fruit freq hash map
		while freq_map.length > 2
			puts("		We have out of lenght for frequencies map. We need to shrink the window")
			left_fruit = tree[window_start]
			freq_map[left_fruit] -= 1
			if freq_map[left_fruit] == 0
				freq_map.delete(left_fruit)
			end
			puts("			We deleted item : ", left_fruit)
			window_start += 1 #shrink the window
		end


		puts("Current Window : ", tree[window_start..window_end+1])
		max_lenght = [max_lenght, window_end - window_start + 1].max
		puts("max_lenght : ", max_lenght)
		puts("-----------------------")
	end
	return max_lenght
	
end


tree = ['A', 'B', 'C', 'B', 'B', 'C']
res = total_fruit(tree)
puts("res : ", res)

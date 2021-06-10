'''	
	We can apply sliding window approach for this question.
	We need a hash map ,to keeping fruit frequecy.

	like  : [1,2,3,2,2]
	we can start in a interate 

	window_start = 0 
	if we have items in hash map we can increment currrent item 


	1 = {1:1}

	1,2 {1:1, 2:1}

	1,2,3 {1:1, 2:1, 3:1}

	we have 3 so length grater than 2 frequencies we need to start to shrink our window , because max we can put 2 different fruits in the basket.

		max_lenght = max(max_len, window_end - window_start + 1)  > 2 
		
		we need to decrement our freq. if current item is 0, we should delete from freq hashmap


	

'''

from typing import List
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        window_start = 0
        freq_map = {}
        max_lenght = 0

        for window_end in range(len(tree)):
        	
        	right_fruit = tree[window_end]
        	if right_fruit not in freq_map:
        		freq_map[right_fruit] = 0
        	freq_map[right_fruit] += 1
        	print('freq_map : ' , freq_map)

        	#shrink the sliding window, until we are left with 2 fruits in the fruit freq hash map
        	while len(freq_map) > 2:
        		print("		We have out of lenght for frequencies map. We need to shrink the window")
        		left_fruit = tree[window_start]
        		freq_map[left_fruit] -= 1
        		if freq_map[left_fruit] == 0:
        			del freq_map[left_fruit]
        			print("			We deleted item : ", left_fruit)
        		window_start += 1 #shrink the window


        	print("Current Window : ", tree[window_start:window_end+1])
        	max_lenght = max(max_lenght, window_end - window_start + 1)
        	print("max_lenght : ", max_lenght)
        	print("-----------------------")

        return max_lenght


tree = ['A', 'B', 'C', 'B', 'B', 'C']
res = Solution().totalFruit(tree)
print("res : ", res)

'''
	tree = ['A', 'B', 'C', 'B', 'B', 'C'] 


	freq_map :  {'A': 1}
	Current Window :  ['A']
	max_lenght :  1
	-----------------------
	freq_map :  {'A': 1, 'B': 1}
	Current Window :  ['A', 'B']
	max_lenght :  2
	-----------------------
	freq_map :  {'A': 1, 'B': 1, 'C': 1}
			We have out of lenght for frequencies map. We need to shrink the window
				We deleted item :  A
	Current Window :  ['B', 'C']
	max_lenght :  2
	-----------------------
	freq_map :  {'B': 2, 'C': 1}
	Current Window :  ['B', 'C', 'B']
	max_lenght :  3
	-----------------------
	freq_map :  {'B': 3, 'C': 1}
	Current Window :  ['B', 'C', 'B', 'B']
	max_lenght :  4
	-----------------------
	freq_map :  {'B': 3, 'C': 2}
	Current Window :  ['B', 'C', 'B', 'B', 'C']
	max_lenght :  5
	-----------------------
	res :  5
'''
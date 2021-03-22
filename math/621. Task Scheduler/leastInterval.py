'''
	We can apply some Math formula for this position.
	
	like = 
		A,B,C,D,B,A,B,A,A,B

		A B C    A B D    A B IDLE     A B

		first we need max freq in this array.
		we can use an extra freq arr
		this array will be 26 item like letter in alphabe.
		
		arr = [0] * 26

		and we can fill using by chars of ASCI code

		for t in tasks
			freq[ord(t) - ord('A')

		and array will be freq = [4,4,1,1,0,0,0,0,0,0,0 ....]

		A B C    A B D    A B IDLE     A B
		
		we have 3 groups (most item 3)


		max_freq_char = A : 4 , B: 4
		means 
		max_freq_char = 4 
		max_freq_char_count = 2 (A and B)

		our formula will be

		(max_freq_char - 1) * (n+1) + max_freq_char_count
		3 * 3 + 2 = 11

		but in some case this formula computes less than over all the number of tasks. 
		Therefore we need to match and get maxs by the len(tasks) 

'''
from typing import List
class Solution:
	def leastInterval(self, tasks: List[str], n: int) -> int:
	
		freq = [0]*26
		for t in tasks:
			freq[ord(t) - ord('A')] += 1

		max_freq = max(freq)
		print("max_freq : ", max_freq)

		max_freq_count = freq.count(max_freq)
		print("max_freq_count : ", max_freq_count)

		tasks_len = len(tasks)
		freq_tasks_len = ((max_freq - 1)*(n+1)) + max_freq_count

		return max(tasks_len, freq_tasks_len)




tasks = ["A","A","A","B","B","B"]
n = 2

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
res = Solution().leastInterval(tasks, n)
print("res :", res)

'''
	T(N) = O(N Total) N Total is a number of tasks to execute.
	This time is needed to iterate over the input array tasks and to compute the array freq.

	S(N) = O(1) , constant array freq of 26 items.


'''

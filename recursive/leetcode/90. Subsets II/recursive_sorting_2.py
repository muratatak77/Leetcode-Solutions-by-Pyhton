#first we can sort this array
# I will be have sub problem definition and partial solution in recursive approach
# 

'''
I will apply exc and include in a tree for everh each number in array
	nums = 1,2,2

	[],[1],[1,2],[2],[2,2],[1,2,2]

'''

def overall(nums):
	
	result = []
	nums.sort()
	n = len(nums)
	
	def helper(s,i,slate):
		#base cases , leaf node
		if i == n:
			result.append(slate[:])
			return
		else:
			#recursive case, internall nodes
			#count : how many copies of s[i] there are
			count = 0
			for index in range(i,n):
				if s[index] != s[i]:
					break
				count += 1

			#exclude case
			helper(s,i+count,slate)

			#include case
			for _ in range(1,count+1):
				slate.append(s[i])
				helper(s,i+count,slate)

			for _ in range(1,count+1):
				slate.pop()

	helper(nums,0,[])
	return result


nums = [1,2,2]

nums = [4,4,4,1,4]
print(overall(nums))



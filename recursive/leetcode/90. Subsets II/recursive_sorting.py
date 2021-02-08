def overall(nums):
	nums.sort()
	result = []
	n = len(nums)
	print(" N : " , n)
	print(" nums : " , nums)
	print("===================================")
	def helper(s,i,slate):
		#base case : leaf worker nodes
		print(" start >>>>> i :", i, " - slate :", slate)
		if i == n:
			print("result.append : ", slate[:])
			result.append(slate[:])
			return
		else:
		#recursive case : internal nodes
			count=0
			for index in range(i,n):
				if s[index] != s[i]:
					break
				count += 1

			print("count : ", count ," -  i  :  ", i)

			#exclude case
			# print("call exclude case : slate ", slate[:])
			print("======================== 1 call helper ====================  i + count : ", i+count, " - slate : ", slate)
			helper(s,i+count,slate)

			#include case
			for c in range(1,count+1):
				slate.append(s[i])
				print("slate include : ", slate, " - i: ", i, " - count : ", count)
				print("======================== 2 call helper ====================  i + count : ", i+count, " - slate : ", slate)
				helper(s,i+count,slate)

			for c in range(1,count+1):
				print("Slate pop :", slate)
				slate.pop()

	helper(nums,0,[])
	return result

nums = [2,2]

# nums = [4,4,4,1,4]
print(overall(nums))
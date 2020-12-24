def overall(nums,k):

	def helper(s, i=0, sumslate=0 ,count=0):
			
		if count == 0 and k == 0 and sumslate == 0:
			return False

		if i == len(s):
			if sumslate == k:
				return True

			return False
		
		#recursive case 
		return helper(s, i+1, sumslate+s[i], count = count +1) or helper(s, i+1,sumslate, count)
	

	return helper(nums)

arr = [-10000000000,-10000000000,-80000000000,-30000000000,-180000000000,110000000000,60000000000,-90000000000]
k = -90000000000

arr = [1,1,0]
k = 0

print(overall(arr,k))


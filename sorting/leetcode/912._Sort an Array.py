class Solution(object):

	def sortArray(self, nums):
		self.radixSort(nums) 

	def countingSort(self, arr, exp1): 
	
		n = len(arr) 
		print("n : ", n)
		output = [0] * (n)
		print("output : " , output)
		count = [0] * (10)
		print("count  : " , count)

		for i in range(0, n): 
				index = (arr[i]//exp1)
				print("index : ", index)
				count[ (index)%10 ] += 1
				print("count : ", count)
		print("======================")
		for i in range(1,10): 
				count[i] += count[i-1] 
		print("count 2 : ", count)
		print("======================")

		# Build the output array 
		i = n-1
		while i>=0: 
				index = (arr[i]//exp1)
				print("index : ", index)
				print("count[index%10] - 1 : ", count[index%10] - 1)
				output[ count[ (index)%10 ] - 1] = arr[i] 
				print("output : ", output)
				count[ (index)%10 ] -= 1
				print("count :", count)
				i -= 1
	
		i = 0
		for i in range(0,len(arr)): 
				arr[i] = output[i] 

		print("arr: ", arr)
		print("===========================")
	def radixSort(self, arr): 
	
		max1 = max(arr) 

		exp = 1
		while max1//exp > 0: 
				print("exp : ", exp)
				self.countingSort(arr,exp) 
				exp *= 10
		

# Driver code to test above 
arr = [ 170, 45, 75, 90, 802, 24, 2, 66] 
arr = [ 170, 45, 33, 2, 12] 
s = Solution().sortArray(arr)
# s.sortArray(arr) 
	
for i in range(len(arr)): 
		print(arr[i]), 
		
			
			

#Kth largest element is meaning N-kth smallest element
#We can applu quick select alg. that it also same quick sort
#Normally quick sort alg works O(NLogN) but in this case we gonna interest just one side left or right side. hence our alg reduces avarage time complexitiy to  O(N)
#
import random
class Solution():

	def findKthLargest(self,nums,k):

		def select(left, right, k_smallest):
			
			if left == right:
				return nums[left]

			p_idx = partition(left, right)

			if p_idx == k_smallest:
				return nums[p_idx]

			elif p_idx > k_smallest:
				#go to left
				return select(left, p_idx-1, k_smallest)
			else:
				#go the right
				return select(p_idx+1, right, k_smallest)



		def partition(left, right):
			
			pivot_idx = (left+right)//2
			# pivot_idx = random.randint(left,right)
			pivot = nums[pivot_idx]
			
			nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

			store_idx = left
			for i in range(left,right):
				if nums[i]< pivot:
					nums[store_idx], nums[i] = nums[i], nums[store_idx]
					store_idx += 1

			nums[right], nums[store_idx] = nums[store_idx], nums[right]

			return store_idx

		return select(0, len(nums)-1, len(nums)-k)
		

# arr = [7,2,3,5,6,1]
arr = [3,2,1,5,6,4]
k = 2
res = Solution().findKthLargest(arr,k)
print(res)

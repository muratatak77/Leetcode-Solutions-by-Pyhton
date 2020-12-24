#Kth largest element is meaning N-kth smallest element
#We can applu quick select alg. that it also same quick sort
#Normally quick sort alg works O(NLogN) but in this case we gonna interest just one side left or right side. hence our alg reduces avarage time complexitiy to  O(N)
#
class Solution():

	def findKthLargest(self,arr,k):

		def select(left, right, k_smallest):
			
			if left == right:
				return arr[left]

			pivot_index = partition(left, right)

			if pivot_index == k_smallest:
				return arr[k_smallest]
			elif pivot_index > k_smallest:
				#go to left
				return select(left, pivot_index -1 , k_smallest )
			else:
				#go tro right
				return select(pivot_index+1, right, k_smallest )


		def partition(left, right):

			pivot_idx = (left+right)//2
			pivot = arr[pivot_idx]

			#move pivot to the right
			arr[pivot_idx], arr[right] = arr[right],arr[pivot_idx]

			#moved all numbers to the left that less than pivot
			store_idx = left
			for i in range(left, right):
				if arr[i] < pivot:
					arr[store_idx] ,arr[i]= arr[i], arr[store_idx]
					store_idx += 1

			#moved to the pivot idx 
			arr[right], arr[store_idx] = arr[store_idx], arr[right]
			return store_idx

		
		return select(0, len(arr)-1 , len(arr)-k)
		

# arr = [7,2,3,5,6,1]
arr = [3,2,1,5,6,4]
k = 2
res = Solution().findKthLargest(arr,k)
print(res)

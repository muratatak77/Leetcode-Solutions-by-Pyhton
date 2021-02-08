import random

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right):
            print("We'll process: ", nums[left:right+1])
        	# select a random pivot_index between 
            pivot_index = random.randint(left, right)     
            # pivot_index = (left+right)//2

            pivot = nums[pivot_index]
            print("pivot : " + str(pivot))
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            print("nums : " + str(nums))

            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
            	print("nums[i] : " + str(nums[i]) , " < pivot :", pivot)
            	if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    print("changed : ", nums[store_index] , nums[i])
                    store_index += 1

            print("store_index : ", store_index)
            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            print("final arr : ", nums )
            print("=============================")
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                print("left == right ", left , " == ", right)
                return nums[left]   # return that element
            
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right)
            print("got pivot_index : ", pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                print("we found it k_smallest :", k_smallest , " - pivot_index : ", pivot_index)
                return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                print("k_smallest < pivot_index")
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                print("k_smallest > pivot_index")
                return select(pivot_index + 1, right, k_smallest)


        # kth largest is (n - k)th smallest 
        return select(0, len(nums) - 1, len(nums) - k)


# arr = [7,2,3,5,6,1]
arr = [3,2,1,5,6,4]
k = 2
res = Solution().findKthLargest(arr,k)
print(res)

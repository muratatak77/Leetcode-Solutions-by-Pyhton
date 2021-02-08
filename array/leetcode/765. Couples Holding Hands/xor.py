'''
	We can apply XOR bitwise operator for this question
	if a person is number x, their partner is x^1, where ^ is the bitwise XOR operator.
	for each first person 
		x = row[i]
		if we have an match row[i+1] == x^1
			we don't do nothing just contunie

		if it doesn't match 
			we can iterate start current index+1 to len(row)
				if row[j] == x^1:
					swap(row[i+1],row[j])
					break

 	row = [0, 2, 1, 3]

 	i = 0,  item = 0,  should be (item+1)^1 = 1 but we have 2
 		
 		we can increment global ans here because end of the next iterate process we will get just 1 increment

 		we start to iterate i+1 item , so 2 
 		2 is not equal 
 		we can reach 1 ok we got match
 			we can swap current item and match item
			row will be : [0,1,2,3]
			and we have to break


	i = 2, item = 2 , next item 3 
		match item+1^1 == 3

	return answer
'''

from typing import List
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        
        ans = 0
        n = len(row)
        for i in range(0,n,2):
        	x = row[i]
        	if row[i+1] == x^1:
        		continue

        	ans += 1
        	for j in range(i+1,n):
        		if row[j] == x^1:
        			row[x+1], row[j] = row[j], row[x+1]
        			print("After swap : ", row)
        			break
        return ans

row = [0, 2, 1, 3]
res = Solution().minSwapsCouples(row)
print("res : ", res)


'''
	T(N) = O(N^2) couple iterate
	S(N) = O(1) no extra space 
'''


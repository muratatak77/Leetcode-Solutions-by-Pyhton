'''
	we can apply sliding window approaching. We have fix lenght = X

	First in itial : we can find # angry customers customers(0..X) and for all entry array satifsied customers (0..n).




'''
from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        
        numangry = 0
        for i in range(X):
        	if grumpy[i] == 1:
        		numangry += customers[i]

        numsatisfied = 0
        for i in range(len(grumpy)):
        	if grumpy[i] == 0:
        		numsatisfied += customers[i]

        globalmax = numangry

        print("numsatisfied : ", numsatisfied)
        print("numangry : ", numangry)

        print("=========================")

        for i in range(X, len(grumpy)):

        	print("	i : " , i , " - grumpy[i] : ", grumpy[i])

        	if grumpy[i] == 1:
        		numangry += customers[i]
        		print("		numangry increased : ", numangry)

        	if grumpy[i-X] == 1:
        		numangry -= customers[i-X]
        		print("		numangry decreased : ", numangry)

        	globalmax = max(globalmax, numangry)
        	print("				globalmax : ", globalmax)
        	print("=========================")


        return globalmax + numsatisfied


customers = [1,0,1,2,1,1,7,5]
grumpy =    [0,1,0,1,0,1,0,1]
X = 3

res = Solution().maxSatisfied(customers, grumpy, X)
print("res : ", res)
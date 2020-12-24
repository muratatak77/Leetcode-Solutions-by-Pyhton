'''
	we can use dp approach for this problem
	we can use 2D array but finally we need just min use coins size thats way we can use just a memoization table so just array amont of total size.
	
		dp = [0,1,2,3,4,5,6,7,8,9,10,11]

		we can apply bottom up approach and 1 memoization table.

		we can 2 make to loops 

		  for coin in coins:

		  	for x in range(coin, amount+1)
	

			    coin = 1
				x = 1
				how many coin make total  = 1 , answer is just 1
				dp[x] = 1

				coin = 2
				x = 1
				how many 1 coin make total  = 2 , answer is just 2
				dp[x] = 2
	
				.
				.
				.


				coin = 5
				x = 10
				how many 5 coin make total  = 10 , answer is just 2
				dp[x] = 2

	
				we can apply an formula : 
				if we look dp table we can back as coin and +1 and we need min with the current dp item 
				
				dp[x] = min(dp[x], dp[x-coin]+1)



		
		and finally min() function gathers in the last element  
		and we can return directly dp[amount]


'''

from typing import List
import sys

class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		# dp = [float('inf')] * (amount+1)
		dp = [sys.maxsize] * (amount+1)
		dp[0] = 0

		for coin in coins:
			for x in range(coin, amount+1):
				dp[x] = min(dp[x], dp[x-coin]+1)

		if dp[amount] != sys.maxsize:
			return dp[amount]
		else:
			return -1


coins = [1,2,5]
amount = 11

res = Solution().coinChange(coins, amount)
print("res : ", res)


'''
	T(N) = O(S x N)  N : domaniation count.  S : Total of iteration i

	S(N) = O(S) we have just 1 memoization table
'''
from typing import List

class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		dp = [float('inf')] * (amount + 1)
		
		print("generate dp : ", dp )

		dp[0] = 0
		
		print("dp 1 : ", dp)
		
		for coin in coins:
			print("coin : ", coin)
			for x in range(coin, amount + 1):
				print("   x : ", x)

				dp[x] = min(dp[x], dp[x - coin] + 1)
				print("   coin : ", coin)
				print("   x - coin : ", x - coin)
				print("   dp[x - coin] + 1 : ", dp[x - coin] + 1)
				print("	  dp[x] : ", dp[x])
				print("	  dp : ", dp)
				print("=========")
		
			print("===--------------- -------------- --------======")

		return dp[amount] if dp[amount] != float('inf') else -1 




coins = [1,2,5]
amount = 11

res = Solution().coinChange(coins, amount)
print("res : ", res)
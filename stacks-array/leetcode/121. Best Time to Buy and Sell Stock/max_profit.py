class Solution(object):
	"""
	we have peaks and valleys in problem.
	We need to find largest peak following the smallest valley.
	We can maintain 2 variables - minPrice and maxProfit corresponding to the smallest valley and max profit
	We can get max difference beetween selling price and minPrice

	"""

	def maxProfit(prices):

		minPrice = prices[0]
		maxProfit = 0

		for i in range(len(prices)):
			if prices[i] < minPrice:
				minPrice = prices[i]
			elif prices[i] - minPrice > maxProfit:
				maxProfit = prices[i] - minPrice

		return maxProfit

prices = [7,1,5,3,6,4]
mp = Solution.maxProfit(prices)
print(mp)
'''
    we can iterate prices .
        we can store min_price and max_profit variable
        min price first can be max int. 
        max_profit = 0
'''

import sys
class Solution(object):
    def maxProfit(self, prices):

        minPrice = sys.maxsize
        maxProfit = 0

        print("minPrice : ", minPrice)

        for i in range(len(prices)):
            print(" i: " , i)
            print(" prices[i] : ", prices[i])
            if prices[i] < minPrice:
                minPrice = prices[i]
                print("   minPrice : ", minPrice)

            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i]-minPrice

                print("        maxProfit : ", maxProfit)

            print("=====================")

        return maxProfit



prices = [7,1,5,3,6,4]
res = Solution().maxProfit(prices)
print("res : ", res)

'''
 T(N) = O(N) N = lenght of the prices array
 S(N) = O(1) we don't have any extra space

'''
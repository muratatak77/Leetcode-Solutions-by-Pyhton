# '''

#     [7,1,5,3,6,4]

#     sell-7 , buy-1, sell-5, buy-3, sell-6, buy-4

#     sel6 - buy1 = 5 max profit 

#     we can match everytime what is max profit ? 

#     we can iterate prices .
#         we can store min_price and max_profit variable
#         min price first can be max int. 
#         max_profit = 0

#     you can see screen shot.
# '''


class Solution
    def maxProfit(prices)
        
        min_price = (2**(0.size * 8 - 2) -1)
        max_profit = 0
        puts ""

        for i in 0..prices.size-1
            print("i : ", i)
            puts ""
            if prices[i] < min_price
                min_price = prices[i]
            elsif prices[i] - min_price > max_profit
                max_profit = prices[i] - min_price
            end
        end

        return max_profit
    end
end

# import sys
# class Solution(object):
#     def maxProfit(self, prices):

#         minPrice = sys.maxsize
#         maxProfit = 0

#         print("minPrice : ", minPrice)

#         for i in range(len(prices)):
#             print(" i: " , i)
#             print(" prices[i] : ", prices[i])
#             if prices[i] < minPrice:
#                 minPrice = prices[i]
#                 print("   minPrice : ", minPrice)

#             elif prices[i] - minPrice > maxProfit:
#                 maxProfit = prices[i]-minPrice

#                 print("        maxProfit : ", maxProfit)

#             print("=====================")

#         return maxProfit



prices = [7,1,5,3,6,4]
sl = Solution.new()
res = sl.maxProfit(prices)
print " res : ", res
puts ""

# '''
#  T(N) = O(N) N = lenght of the prices array
#  S(N) = O(1) we don't have any extra space

# '''
class Solution:
    def myPow(self, x: float, n: int) -> float:

    	if n == 0:
    		return 1

    	if n < 0:
    		x = 1/x
    		n = -n

    	ans = 1
    	for i in range(n):
    		ans = ans * x

    	return ans


x = 2
n = 3

# x = 2.10000
# n = 3

# x = 2.00000
# n = -2

# x = 0.00001
# n = 2147483647

res = Solution().myPow(x, n)
print("res :", res)

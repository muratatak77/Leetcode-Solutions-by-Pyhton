class Solution:
	def countPrimes(self, n: int) -> int:
		if n < 3:
			return 0

		count = 0
		for num in range(n):
			if num > 1:
				if num == 2:
					count += 1
					continue

				for i in range(2,num):
					if num % i == 0:
						break
				else:
					count += 1

		return count


n = 10
res = Solution().countPrimes(n)
print("res : ", res)
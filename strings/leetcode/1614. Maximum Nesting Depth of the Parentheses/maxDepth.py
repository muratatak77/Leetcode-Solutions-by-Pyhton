class Solution:
		def maxDepth(self, s: str) -> int:
			
			count = 0
			max = 0
			
			if s == '1':
					return 0
			
			for x in s:
					if x == '(':
							count += 1
							if max < count:
									max = count               
					elif x == ')':
							count -= 1
							
			return max


s = "(1+(2*3)+((8)/4))+1"
res = Solution().maxDepth(s)
print("res : ", res)
class Solution(object):
	def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		res = self.nextSequence(n, ['1', 'E'])
		print("result last : ", res)
		return ''.join(res)

	def nextSequence(self, n, prevSeq):
		print("n : ", n , " - prevSeq : ", prevSeq)
		if n == 1:
			return prevSeq[:-1]

		nextSeq = []
		prevDigit = prevSeq[0]
		digitCnt = 1

		print("prevDigit  1 : ", prevDigit)
		for digit in prevSeq[1:]:
			print("		digit : ", digit)
			if digit == prevDigit:
				digitCnt += 1
				print("		digitCnt : ", digitCnt)

			else:
				# the end of a sub-sequence
				print("			digitCnt : ", digitCnt)
				nextSeq.extend([str(digitCnt), prevDigit])
				print("			nextSeq : ", nextSeq)

				prevDigit = digit
				print("			prevDigit 2 : ", prevDigit)

				digitCnt = 1
				print("			digitCnt : ", digitCnt)
			print("----------------------------")

		# add a delimiter for the next sequence
		nextSeq.append('E')
		print("				nextSeq add E: " , nextSeq)
		print("===========================================")
		return self.nextSequence(n-1, nextSeq)


n = 4
res = Solution().countAndSay(n)
print("res : ", res)
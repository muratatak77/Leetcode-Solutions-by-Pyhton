class Solution:
	def combinationSum(self, candidates, target):

		results = []

		def backtrack(remain, start, slate):
			print("remain : ", remain, " /  start : ", start)

			if remain == 0:
				# make a deep copy of the current slateination
				results.append(list(slate))
				return
			elif remain < 0:
				# exceed the scope, stop exploration.
				return

			for i in range(start, len(candidates)):
				# add the number into the slateination
				slate.append(candidates[i])
				# give the current number another chance, rather than moving on
				print(" i : ", i)
				print("call backtrack :  remain - candidates[i] : ",  remain, " - " , candidates[i], " - slate :" , slate )
				backtrack(remain - candidates[i], i, slate)
				# backtrack, remove the number from the slateination
				print("   - pop - ")
				slate.pop()

		
		backtrack(target, 0, [])
		
		return results


candidates = [3,4,5]
target = 8
res = Solution().combinationSum(candidates, target)
print("res : ", res)
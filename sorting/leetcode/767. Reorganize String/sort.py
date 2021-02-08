class Solution(object):
	def reorganizeString(self, S):
		N = len(S)

		pq = [(-S.count(x), x) for x in set(S)]
		print(pq)

		# for c, x in sorted((S.count(x) , x) for x in set(S)):
		# 	if c > (N+1)/2: return ""


		# count = []

		# for s in S:
		# 	hmap[s] = hmap[s] + 1


		# print(hmap)



		
		A = []
		for c, x in sorted((S.count(x), x) for x in set(S)):
			if c > (N+1)/2: return ""
			A.extend(c * x)
			print(A)
		ans = [None] * N
		ans[::2], ans[1::2] = A[N/2:], A[:N/2]
		return "".join(ans)



s="aab"
res = Solution().reorganizeString(s)
print(res)
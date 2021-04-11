'''
	we can generate 5 items answer array
	ans = [1,1,1,1,1]

	we need to have 2 iterator.

	first iterator pass just n. 
	Everytime start 2, because  we have everytime first will be 1 end of the array.
	for i in range(2,n+1)

		second will be a backdraw iterator. 
			start 3 
			we will get sum ans[3] + ans[4] and we can set ans[3]
			ans[3] += ans[4]

			we can contunue iteration 
			ans[2] += ans[3]

			so on...


		n = 1 >> 
			ans = [1,1,1,1,1] = 5 

		n = 2 >> 
			ans = [1,1,1,2,1]
			ans = [1,1,3,2,1]
			ans = [1,4,3,2,1]
			ans = [5,4,3,2,1] 5+4+3+2+1 = 15

		n = 3
			ans = [5,4,3,2,1]
			ans = [15,10,6,3,1]  = 35
'''

class Solution:
	def countVowelStrings(self, n: int) -> int:

		ans = [1] * 5
		print("ans : ", ans)

		for i in range(2,n+1):
			print(" i : ", i)

			for j in range(3,-1,-1):
				print("     j : ", j)
				ans[j] += ans[j+1]

			print("		ans : ", ans)


		print("final ans : ", ans)
		return sum(ans)



n = 3
res = Solution().countVowelStrings(n)
print("res :", res)

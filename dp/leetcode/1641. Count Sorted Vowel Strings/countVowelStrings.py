class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        def helper(n,vowels):
        	#base case, leaf nodes
        	print(" n : ", n , " - vowels : ", vowels)
        	if n == 0:
        		print("	return 1")
        		return 1

        	#recursive case
        	i = vowels
        	result = 0
        	while i<=5:
        		print("		Call helper. n-1 :", n-1, " - i : ", i)
        		result += helper(n-1,i)
        		print("		result : ", result)
        		i += 1
        		print("----------------------------------------")
        	return result


        return helper(n,1)

n = 2
res = Solution().countVowelStrings(n)
print("res :", res)

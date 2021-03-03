'''

'''
class Solution:
	def decodeString(self, s: str) -> str:

		result = []
		
		def dfs(s, i):
			curr_str = ""
			while i < len(s):
				if s[i].isdigit():
					count_str = ""
					while s[i] != "[":
						count_str += s[i]
						i+=1
					count = int(count_str)
					i+=1
					i, substr = dfs(s,i)
					curr_str += (count*substr)
				elif s[i] == "]":
					i+=1
					return i, curr_str
				else:
					curr_str += s[i]
					i+=1
				print("-----------------------------")

			result.append(curr_str)

		dfs(s,0)
		return ''.join(result)


		
# s = '12[a2[c]]'
s = "3[a2[c]]"
# s = "2[abc]3[cd]ef"
res = Solution().decodeString(s)
print("res:", res)
'''
	T(N) = O(N) N is length of string
	S(N) = O(N) 

'''
'''
	https://www.youtube.com/watch?v=IhJgguNiYYk&ab_channel=KevinNaughtonJr.

	We can solve to keep i and j,
	First step 
		we can walk trough i and j in the first char.

		a   ,  a  ,  b ,  b ,   c ,  c ,  c 
		i,j

		a   ,  a  ,  b ,  b ,   c ,  c ,  c 
		i      j

		a   ,  a  ,  b ,  b ,   c ,  c ,  c 
		i            j
			is not same i and j
			bring to i j's position
			and what is diff j-1 = 2
			
			we can change index+1 : 1  => chars[index] = chars[j] 
			new array : a  , a , b ,b,  c ,  c ,  c 
			and must be j-i > 1 everytime. because if we have just one char . like = [a] we can not add any element like  [a,1]

			if (j-i) > 1 
				for c in str(j-i):
					index += 1 = 2
					chars[index] = c

			['a', '2', 'b', 'b', 'c', 'c', 'c']

 

		a   ,  2  ,  b ,  b ,   c ,  c ,  c 
		            i, j
				
				['a', '2', 'b', '2', 'c', 'c', 'c']


		a   ,  b  ,  b ,  b ,   c ,  c ,  c 
					 i	  		j		            
					
					j-i = 4-2 = 2
					we can change index+1 : 2  => chars[index] = chars[j] 
					a   ,  b  ,  c ,  b ,   c ,  c ,  c 

					['a', '2', 'b', '2', 'c', '3', 'c']
		

'''

from typing import List
class Solution:
	def compress(self, chars: List[str]) -> int:

		index = 0
		i = 0
		while i < len(chars):
			j = i
			while j < len(chars) and chars[j] == chars[i]:
				j += 1
				print(" j : ", j)

			#["a","a","a","b","b","a","a"] in this case we need chars[index] = chars[i]
			#['a', '3', 'a', 'b', 'b', 'a', 'a']
			#['a', '3', 'b', '2', 'b', 'a', 'a']
			#['a', '3', 'b', '2', 'a', '2', 'a']
			chars[index] = chars[i]  

			print("chars : ", chars)
			print("index : ", index)


			index += 1
			if (j-i>1):
				for c in str(j-i):
					chars[index] = c
					index+=1
					print("			chars : ", chars)
			print("------------------------------------")

			i = j
			print(" i = j / i :", i, " j : ", j)
			print("chars : ", chars)

		return index


chars = ["a","a","b","b","c","c","c"]
# chars = ["a"] 
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars = ["a","a","a","b","b","a","a"]
res = Solution().compress(chars)
print("res : ", res)
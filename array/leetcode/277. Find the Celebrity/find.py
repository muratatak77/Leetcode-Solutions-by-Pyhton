'''
Question : 
uppose you are at a party with n people (labeled from 0 to n - 1), and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.
 
Example 1:

Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.

------------------------------------------------------------
Solution : 
	
	first : we can find an item possibility whether celebrity or not by making an iterate.

		celebrity_candidate = 0
		for i in range(1, n):
			#if celebrity_candidate knows ith person, ith person would be new celebrity candidate
	    	if knows(celebrity_candidate, i):
	        	celebrity_candidate = i

		We can find which person (0,1,2) would be celebrity candidate person

	second : we need to make verification already celebrity candidate found item from first step

		if already celebrity person knows any other person , means there is no celebrity person in this party.
		if already celebrity person doens't knows any other person , means there is celebrity person.

		for i in range(n):
			if celebrity_cand != i:
				if self.knows(celebrity_cand, i) or not self.knows(i, celebrity_cand):
					return -1
		return celebrity_cand
'''

class Solution:

	def __init__(self,arr):
		self.arr  = arr
	
	def knows(self, i,j):
		return self.arr[i][j] == 1

	def findCelebrity(self, n: int) -> int:
		
		celebrity_cand = 0

		for i in range(1,n):
			print(" i : ", i, "- celebrity_cand: ", celebrity_cand)
			if self.knows(celebrity_cand, i):
				celebrity_cand = i

		print("		celebrity_cand : " , celebrity_cand)

		#verification
		for i in range(n):
			if celebrity_cand != i:
				if self.knows(celebrity_cand, i) or not self.knows(i, celebrity_cand):
					return -1

		return celebrity_cand

n = 3
graph = [[1,1,0],[0,1,0],[1,1,1]]
# graph = [[1,0,1],[1,1,0],[0,1,1]]

res = Solution(graph).findCelebrity(n)
print("res : ", res)

'''
	T(N) = O(N) we have 2 seperate 
	O(N) = O(1)
'''


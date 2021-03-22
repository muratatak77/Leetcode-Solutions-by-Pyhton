'''
accounts = [
	
	["John", "johnsmith@mail.com", "john00@mail.com"], 
	["John", "johnnybravo@mail.com"], 
	["John", "johnsmith@mail.com", "john_newyork@mail.com"], 

	["Mary", "mary@mail.com"]]

Result :

	[

	["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  
	["John", "johnnybravo@mail.com"], 
	["Mary", "mary@mail.com"]]

----------------------------------------------------------------------------

Solving :


We need to connect each email goes to another emails , generate a graph like neighbors list
Connections between email list like a graph adjacent list

We can seperate 2 cases 
1. Constructer graph and email to name hash map relation
	Graph : 
	{
		 'johnsmith@mail.com': {'john_newyork@mail.com', 'john00@mail.com', 'johnsmith@mail.com'},
		 'john00@mail.com': {'johnsmith@mail.com'}, 
		 'johnnybravo@mail.com': {'johnnybravo@mail.com'}, 
		 'john_newyork@mail.com': {'johnsmith@mail.com'}, 
		 'mary@mail.com': {'mary@mail.com'}
	}

	we will generate together email_to_name hashmap

	email_to_name :{
					'johnsmith@mail.com': 'John', 
					'john00@mail.com': 'John', 
					'johnnybravo@mail.com': 'John', 
					'john_newyork@mail.com': 'John', 
					'mary@mail.com': 'Mary'
				}

2. we can apply BFS - Bread First Search.
	We can use a stack keep and to find graph edge and neighbours.
	We can add a compnonent array for  email and  in the each level neighbours.

'''
from collections import defaultdict
class Solution(object):
	def accountsMerge(self, accounts):

		em_to_name = {}
		graph = defaultdict(set)

		for acc in accounts:
			name = acc[0]

			print("	name : ", name)
			print("	acc[1:] : ", acc[1:])

			for email in acc[1:]:

				print("		acc[1] : ", acc[1])
				graph[acc[1]].add(email)
				print("		graph 1 : ", graph)

				print("		email : ", email)
				graph[email].add(acc[1])
				print("		graph 2 : ", graph)

				em_to_name[email] = name
				print("		em_to_name : ", em_to_name)

		print("GRAPH : ", graph)
		print("em_to_name : ", em_to_name)
		print("-------------------------------")

		seen = set()
		ans = []
		for email in graph:
			if email not in seen:
				print("EMAIL : ", email)
				seen.add(email)
				stack = [email]
				print(" stack : ", stack)
				component = []
				while stack:
					node = stack.pop()
					print(" 	node : ", node)

					component.append(node)
					print(" 	component : ", component)

					for nei in graph[node]:
						print(" 	nei : ", nei)

						if nei not in seen:
							seen.add(nei)
							stack.append(nei)
				ans.append([em_to_name[email]] + sorted(component))
				print("ANS : ", ans)
		
		print("======== ----- =================-- ============== ")

		return ans

accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

res = Solution().accountsMerge(accounts)
print("res : ", res)
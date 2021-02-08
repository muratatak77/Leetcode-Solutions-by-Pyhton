from typing import List
from collections import defaultdict

class Solution:
	def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

		graph = defaultdict(defaultdict)
		print("Initial graph :", graph)

		# Step 1). build the graph from the equations
		for (dividend, divisor), value in zip(equations, values):
			# add nodes and two edges into the graph
			graph[dividend][divisor] = value
			graph[divisor][dividend] = 1 / value
		
		print("Fill up graph :", graph)
		print("========================")



		def backtrack_evaluate(curr_node, target_node, acc_product, visited):
			visited.add(curr_node)
			print("				visited add curr_node : ", curr_node, "- acc_product : ", acc_product, " - target_node : ", target_node)
			ret = -1.0
			neighbors = graph[curr_node]
			print("				neighbors : ", neighbors)
			if target_node in neighbors:
				print("					target_node in neighbors")
				ret = acc_product * neighbors[target_node]
				print("					ret :", ret)
			else:
				for neighbor, value in neighbors.items():
					print("				neighbor : ", neighbor , " - value : ", value)
					if neighbor in visited:
						print("				neighbor in visited continue. neighbor :" ,neighbor, " visited :", visited)
						continue
					ret = backtrack_evaluate(neighbor, target_node, acc_product * value, visited)
					print("				ret : ", ret)
					if ret != -1.0:
						break

			print("					visited before removing : ", visited)
			visited.remove(curr_node)
			print("					visited remove curr_node : ", visited)
			print("					return ret : ", ret)

			return ret

		# Step 2). Evaluate each query via backtracking (DFS)
		#  by verifying if there exists a path from dividend to divisor
		results = []
		for dividend, divisor in queries:
			if dividend not in graph or divisor not in graph:
				print("     dividend or divisor not in graph. dividend :", dividend, " = divisor :", divisor)
				# case 1): either node does not exist
				ret = -1.0
			elif dividend == divisor:
				print("      dividend == divisor. dividend : ", dividend , " - divisor :", divisor)
				# case 2): origin and destination are the same node
				ret = 1.0
			else:
				visited = set()
				print("			Call DFS, dividend - curr_node :" , dividend, " - divisor - target_node : ", divisor, " - acc_product : 1 , visited : ", visited)
				ret = backtrack_evaluate(dividend, divisor, 1, visited)

			print("    results append : ", ret)
			results.append(ret)
			print("results : ", results)

		return results



equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

res = Solution().calcEquation(equations, values, queries)
print("res : ", res)
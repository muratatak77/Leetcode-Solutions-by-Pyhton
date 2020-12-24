from collections import defaultdict
class Solution:

	WHITE = 1
	GRAY = 2
	BLACK = 3

	def findOrder(self, numCourses, prerequisites):
		
		# Create the adjacency list representation of the graph
		adj_list = defaultdict(list)

		print("initial adj_list : ", adj_list)

		# A pair [a, b] in the input represents edge from b --> a
		for dest, src in prerequisites:
			adj_list[src].append(dest)

		print("filling adj_list : ", adj_list)

		topological_sorted_order = []
		is_possible = True

		# By default all vertces are WHITE
		color = {k: Solution.WHITE for k in range(numCourses)}

		print("initial color : ", color)

		def dfs(node):
			nonlocal is_possible

			# Don't recurse further if we found a cycle already
			if not is_possible:
				return

			# Start the recursion
			color[node] = Solution.GRAY
			print("     color in dfs : ", color)
			# Traverse on neighboring vertices
			if node in adj_list:
				for neighbor in adj_list[node]:
					print("neighbor of node : neighbor : ", neighbor ,  " - node : ", node)
					if color[neighbor] == Solution.WHITE:
						print("       color[neighbor] == Solution.WHITE. neighbor = " , neighbor)
						dfs(neighbor)
					elif color[neighbor] == Solution.GRAY:
						print("        color[neighbor] == Solution.GRAY. is possible. neighbor = ", neighbor)
						 # An edge to a GRAY vertex represents a cycle
						is_possible = False

			# Recursion ends. We mark it as black
			color[node] = Solution.BLACK
			print("  color[node = Solution.BLACK. Node : ", node)
			print("  color in dfs : ", color)

			topological_sorted_order.append(node)
			print("  topological_sorted_order : ", topological_sorted_order)
			print("========================================")


		for vertex in range(numCourses):
			print("start vertex : ", vertex)
			# If the node is unprocessed, then call dfs on it.
			if color[vertex] == Solution.WHITE:
				dfs(vertex)

		return topological_sorted_order[::-1] if is_possible else []


numCourses = 2
prerequisites = [[1,0],[0,1]]
# prerequisites = [[1,0]]


numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

numCourses = 5
prerequisites = [[1,0],[2,0],[3,1],[3,2],[2,3]]


ans = Solution().findOrder(numCourses, prerequisites)
print("ans : ", ans)

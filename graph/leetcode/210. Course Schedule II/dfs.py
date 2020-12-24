class Solution(object):
	def findOrder(self, numCourses, prerequisites):

		#build directed graph
		n = numCourses
		adjList = [[] for _ in range(n)]
		for (src, dst) in prerequisites:
			adjList[dst].append(src)
		print("adjList : " , adjList)

		visited = [-1] * n
		arrival = [-1] * n 
		departure = [-1] * n
		timestamp = [0] 
		topSort = []

		#dfs to detect whether cycle found or not
		def dfs(source):
			arrival[source] = timestamp[0]
			timestamp[0] += 1
			visited[source] = 1
			for neighbor in adjList[source]:
				if visited[neighbor] == -1:
					if dfs(neighbor):
						return True
				else:
					if departure[neighbor] == -1:
						#we have cycle
						return True

			topSort.append(source)
			timestamp[0] += 1
			departure[source] = timestamp[0]
			print(topSort)
			return False


		for v in range(n):
			if visited[v] == -1:
				if dfs(v):
					#we found a cycle , you cannot complete the courses
					return []

		return topSort[::-1]

		

numCourses = 2
prerequisites = [[1,0]] 


numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]


numCourses = 2
prerequisites = [[1,0],[0,1]]


ans = Solution().findOrder(numCourses, prerequisites)
print(ans)
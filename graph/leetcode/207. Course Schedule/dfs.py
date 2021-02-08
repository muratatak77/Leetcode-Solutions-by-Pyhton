class Solution:
	def canFinish(self, numCourses, prerequisites):

		# in question desc : "There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1." So, we have walk through left to right. we can't back the any other course.
		# This is a directed graph problem  because we have given n input  (setup n courses) and  pairwise relationship. We can build adjancy list.
		# what exactly prerequisites : meaning if we have cycle in directed graph we can not degree. if we don't have a cycle in directed graph we can degree. 
		# we can apply dfs approach 
		
		#build graph
		n = numCourses

		adjList  = [[] for _ in range(n)]
		for dst,src in prerequisites:
			# adjList[src].append(dst) 
			## we don't use because we have directed graph
			adjList[dst].append(src)

		print("Build adjList : ", adjList)

		# we need  visited array. 
		# arrival time = first visit a vertex  in the dfs call
		# departure time = return back a vertex in dfs call
		# to fill arrival and departure time we need timestamp array
		# if we have departure time not been set yet in a visited vertex this is a cycle. because dfs call is still going. 
	 
		visited = [-1] * n
		arrival = [-1] * n
		departure = [-1] * n
		timestamp = [0]

		print("visited : ", visited)
		print("arrival : ", arrival)
		print("departure : ", departure)
		print("timestamp : ", timestamp)
		print("=============")

		# in dfs method we will try to find a cycle, if we have a cycle we can return True
   
		def dfs(source):
			print("source :", source)
			arrival[source] = timestamp[0]
			timestamp[0] += 1
			visited[source] = 1

			print("departure 1 : ", departure)
			print("arrival 1  : ", arrival)
			print("timestamp 1  : ", timestamp)
			print("=====")

			for neighbor in adjList[source]:
				print("neighbor :", neighbor)
				if visited[neighbor] == -1:
					print("===== Call DFS =====")
					if dfs(neighbor):
						return True
				else:
					print("not visited neighbor : ", neighbor)
					print("departure : ", departure)
					if departure[neighbor] == -1:
					#this is a back edge , hence a Cycle
						return True
			departure[source] = timestamp[0]
			timestamp[0] += 1
			print("departure 2 : ", departure)
			print("arrival 2  : ", arrival)
			print("timestamp 2 : ", timestamp)
			return False


		for v in range(n):
			if visited[v] == -1:
				if dfs(v):
					#if cycle found , you cannot complete the courses
					return False
		return True # No cycle  found anywhere




numCourses = 2
prerequisites = [[1,0],[0,1]]
prerequisites = [[1,0]]


ans = Solution().canFinish(numCourses, prerequisites)
print("ans : ", ans)


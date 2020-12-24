import collections
class Solution:
	def possibleBipartition(self, N, dislikes):
		
		#build graph
		adjList = collections.defaultdict(list)
		for (src, dst) in dislikes:
			adjList[src].append(dst)
			adjList[dst].append(src)
		color = {}
		print("Build adjList : ", adjList)
   
		def dfs(node):
			for nei in adjList[node]:
				print("nei :" , nei)
				if nei not in color:
					color[nei] = 1 - color[node]
					if not dfs(nei):
						return False
				elif color[nei] == color[node]:
					print("heyyy boomm : color  ", color , " nei : ", nei, " - node : ", node)
					print("color[nei] == color[node] : " , color[nei] , " == ", color[node])
					return False
			return True

		#outer loop
		for node in range(1, N+1):
			if node not in color:
				color[node] = 0
				if not dfs(node):
					print("We got false : ", node)
					return False
		return True



N = 4
dislikes = [[1,2],[1,3],[2,4]]
dislikes = [[1,2],[1,3],[2,3]]
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]

ans = Solution().possibleBipartition(N, dislikes)
print(ans)
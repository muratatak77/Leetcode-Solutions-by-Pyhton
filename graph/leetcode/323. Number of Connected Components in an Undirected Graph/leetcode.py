class Solution:
    def countComponents(self, n, edges):
        
        #build graph
        adjlist = [[] for _ in range(n)]
        for (src, dst) in edges:
            adjlist[src].append(dst)
            adjlist[dst].append(src)
            
        #graph will be >  [1],[0,2],[1],[4],[3]
            
        #build visited array
        visited = [False] * (n)
        #visited >> [F, F, F, F, F]
        
        #bfs traversal
        def bfs(source):
            q = collections.deque([source]) #q = 0
            visited[source]=True #visited[0] = T
            while q:
                node = q.popleft() # 0, 1
                for neighbor in adjlist[node]: # 1 
                    if visited[neighbor] == False: 
                        q.append(neighbor) # 1 , 2 
                        visited[neighbor] = True # visited[0,1,2] = T
        #dfs traversal
        def dfs(node):
            visited[node] = True
            for neighbor in adjlist[node]:
                if visited[neighbor] == False:
                    dfs(neighbor)
            
        
        #outer loop
        components = 0
        for v in range(n):
            if visited[v] == False:
                components += 1
                #bfs(v)
                dfs(v)
        return components
                
            
# BFS = 92 ms, faster than 99.43% of Python3
# DFS = 104 ms, faster than 87.18% of Python3 (There are recursive call stacks)

# T(n) = push/pop each vertex from the q + neighbor structer
# T(n) = O(n) + O(m) = O(m+n)
# S(n) = O(n)



n = 5
edges = [[0, 1], [1, 2], [3, 4]]
# edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

        
res = Solution().countComponents(n,edges)
print(res)
